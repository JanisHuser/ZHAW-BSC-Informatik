# Kernel Modules

Basics:

- A programming module with interfaces
- Communication Medium between application/user and hardware → lives in Kernel Space + used for hardware access with minimal functionality 
- can be hot loaded/unloaded - only possible with `root` privileges → actual name "Loadable Kernel Module"
- Gateway to User Space through File Interface with a virtual File (`/sys/..`)

Types:
- Device Drivers
- Filesystem Drivers
- Network Drivers

LKM Utilities Commands:
```bash
# Insert an LKM into the kernel
sudo insmod <module.ko>
# Remove an LKM from the kernel
sudo rmmod <module>
# List currently loaded LKMs
sudo lsmod
# Display information of LKM object file
sudo modinfo <module.ko>
# Insert or remove an LKM, when in /lib/modules
sudo modprobe
```

Discoverable Hardware
- PCI/USB devices are discoverable.
- When connecting a device to a bus, it receives a unique identification used for communication with the CPU.
- PCI/USB devices tell the system what sort of device they are

Non-discoverable Hardware
- Simple Interfaces (I2c or SPI) are not discoverable
- Such hardware has to be explicitly defined → in Device Tree
- Kernel Modules communicating with the Device Tree are called → **Platform Drivers**

## Concept 

![alt text](media/concept%20-%20Kernel%20Module.png)

![alt text](media/concept%20-%20Kernel%20Module%20-%20structure.png)

## 1. Simple LKM

Minimal viable LKM:
```c
#include <linux/kernel.h>
#include <linux/module.h>

// init function
static int __init my_module_init(void) {
	...
}

// exit function
static void __exit my_module_exit(void) {
	...
}

/*
* The next calls are mandatory -- they identify the initialization
* and the cleanup function (as above).
*/
module_init(my_module_init);
module_exit(my_module_exit);

/* Kernel module description */
MODULE_LICENSE("GPL");
MODULE_AUTHOR("Vladimir Lenin");
MODULE_DESCRIPTION("A desc.");
MODULE_VERSION("1.0");

```
C does not have namespace-functionality → naming conflicts/pollition possible  
Avoid Kernel namespace pollution: always use `static` for global vars. to give it file internal linkage

## 2. Platform Driver

- Defines a data structure that keeps track of device state.
- Implements a set of helper functions, interrupt handlers, etc.
- Defines a `probe()` method
- Similarly defines a corresponding `remove()` method
- Registersthe device to the Kernel in the `__init` method
- Similarly unregisters the device in the `__exit` method

### Prob:  
Input: a structure describing the device:
```C
int driver_probe(struct platform_driver *pdev)
```
- Initializes device
- Maps I/O memory
- Registers Interrupt Handlers
- Starts Kernel Threads
- Registers device to proper kernel framework

### Remove
Input: a structure describing the device:
```C
int driver_remove(struct platform_driver *pdev)
```
- No general responsibilities → open to implementation

### Registration 
Put everything together with LKM:
- define `probe` and `remove` functions
- declare them in Platform Driver Definition
- Un-/Register Platform Driver Definition using `__exit` and `__init` methods

```c
#include <linux/platform_device.h>
#include <linux/mod_devicetable.h>

// Example struct device desc.
struct platform_driver {
	int (*probe) (structplatform_device *);
	int (*remove) (structplatform_device *);
	void (*shutdown) (structplatform_device *);
	int( *suspend) (structplatform_device *, pm_message_tstate);
	int (*resume) (structplatform_device *);
	struct device_driverdriver;
	const struct platform_device_id *id_table;
};

// Initialization Platform Driver Definition
static struct platform_driver sevenseg_driver = {
    .driver = {.name = "sevenseg",
               .owner = THIS_MODULE,
			   .of_match_table = sevenseg_device_tree_ids, // see point "3. Platform Driver with Device Tree"
	},
    .probe = sevenseg_probe,     // Declare probe function
    .remove = sevenseg_remove    // Declare remove function
};

static int sevenseg_probe(struct platform_device *pdev) {
	...
}

static int sevenseg_remove(struct platform_device *pdev) {
	...
}

// registration
static int __init sevenseg_init(void) {
    platform_driver_register(&sevenseg_driver);
    return 0;
}

static void __exit sevenseg_exit(void) {
    platform_driver_unregister(&sevenseg_driver);
}
```

## 3. Platform Driver with Device Tree

Platform Driver has to be linked somehow to the correct device node in the Device Tree

In Device Tree:
```c
sevenseg {
	compatible = "sevenseg"; //<---- searched string
}
```

In Platform Driver:
```c
...
static const struct of_device_id sevenseg_device_tree_ids[] = {
    {
        .compatible = "sevenseg",
    },
    {}};

MODULE_DEVICE_TABLE(of, sevenseg_device_tree_ids);

static struct platform_driver sevenseg_driver = {
    .driver = {.name = "sevenseg",
               .owner = THIS_MODULE,
			   .of_match_table = sevenseg_device_tree_ids, // <----- look here
	},
    .probe = sevenseg_probe,     // Declare probe function
    .remove = sevenseg_remove    // Declare remove function
};
....
```

## 4. Access Hardware Device

- Use global data structure for information exchange between methods
- Use `prob` function to allocate memory and register `struct`

```c
...

/*
 * Type definitions and global variables for kernel module
 */
typedef struct sevenseg_platform_data {
    struct device* dev;
    int counter;
    int mode;
    void __iomem* base_addr;
    int irq;
    struct task_struct* kthread_sevenseg;
} sevenseg_platform_data;

...

static int sevenseg_probe(struct platform_device *pdev) {
	struct sevenseg_platform_data* pdata;
	...
	pdata = devm_kzalloc(&pdev->dev, sizeof(pdata), GFP_KERNEL); // allocate memory
	platform_set_drvdata(pdev, pdata); // register bzw. set struct as "driver data"
	...
}
```

![alt Text](media/devTree-%20Kernel%20Module.png)

How to get resource and virtual address from Device Tree, implement in `prob` function:
```c
static int sevenseg_probe(struct platform_device* pdev) {
    struct sevenseg_platform_data* pdata;
    struct resource* res;
	...
    res = platform_get_resource(pdev, IORESOURCE_MEM, 0); // <-------- get resource from Device Tree
    if(res == NULL) {
        pr_err("platform_get_resource() failed! \n");
        return -1;
    }
    pr_info("Info: 35Bit ARM Address: 0x%x \n", res->start);

    pdata->base_addr = devm_ioremap_resource(&pdev->dev, res); // <-------- get virtual address
    if(IS_ERR(pdata->base_addr)) {
        pr_err("Error: devm_ioremap_resource() failed! \n");
        return PTR_ERR(pdata->base_addr);
    }
    pr_info("Info: Virtual Address: 0x%x \n", pdata->base_addr);

    ...

    return 0;
}
```

Write to Peripheral: `void iowrite{$X$}(u{$X$} value, void* addr);`
Read from Peripheral: `void ioread{$X$}(void* addr);`

With `{$X$}` = `8` or `16` or `32`

Example usage in device setup:
```c
static int sevenseg_probe(struct platform_device* pdev) {
    struct sevenseg_platform_data* pdata;
    struct resource* res;
	...
    // Configure different GPIOs
    // Setup keys as GPIO_IN
    init_gpio(pdata, keys[1], GPIO_IN);              	 // <----- uses iowrite32 & ioread32
    set_trigger_gpio(pdata, keys[1], GPIO_EDGE_FALLING); // <----- uses iowrite32 & ioread32
    
	init_gpio(pdata, keys[0], GPIO_IN);              	 // <----- uses iowrite32 & ioread32
    set_trigger_gpio(pdata, keys[0], GPIO_EDGE_FALLING); // <----- uses iowrite32 & ioread32

    // Setup the two sevenseg's to GPIO_OUT
    for(i = 0; i < 8; i++) {
        init_gpio(pdata, sevensegs[0][i], GPIO_OUT); // <----- uses iowrite32 & ioread32
        init_gpio(pdata, sevensegs[1][i], GPIO_OUT); // <----- uses iowrite32 & ioread32
    }
    // Initialize the sevenseg with the first number
    sevenseg_write(pdata, pdata->counter);			 // <----- uses iowrite32
    dev_info(&pdev->dev, "Info: Finished initializing sevenseg \n");

    ...

    return 0;
}
```

## 5. Create /sys File

Platform Dreiver needs to:
1. provide `store` and `show`functions
2. "register" their function pointers
3. create virtual file in /sys that will be writen to/read from → in `probe` and `remove` functions


![alt tesxt](media/store.show%20-%20Kernel%20Module.png)

1. and 2.
```C
// user writes to file "counter"
static ssize_t counter_store(struct device* dev,
                             struct device_attribute* attr,
                             const char* buf,
                             size_t count) {
	...
}

// user reads from file "counter"
static ssize_t counter_show(struct device* dev,
                            struct device_attribute* attr,
                            char* buf) {
    ...
}

// Macro to define counter and show/store Function
DEVICE_ATTR(counter, 0644, counter_show, counter_store);
```
Location of „File“: `/sys/bus/platform/drivers/sevenseg/fe200000.sevenseg/counter`

3.
```c
static int sevenseg_probe(struct platform_device* pdev) {
    struct sevenseg_platform_data* pdata;
    struct resource* res;
	...
    // Create File "counter"
    ret = device_create_file(&pdev->dev, &dev_attr_counter);    //<----- create
    if(ret != 0) {
        pr_err("device_create_file() failed with: %d() \n", ret);
        return -1;
    }
    ...

    return 0;
}

static int sevenseg_remove(struct platform_device* pdev) {
    struct sevenseg_platform_data* pdata = platform_get_drvdata(pdev);

    device_remove_file(&pdev->dev, &dev_attr_counter); 		  //<----- remove
    kthread_stop(pdata->kthread_sevenseg);

    return 0;
}
```

