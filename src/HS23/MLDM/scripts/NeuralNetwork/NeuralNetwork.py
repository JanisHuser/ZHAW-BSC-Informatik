import random
import math
from numbers import Number
from enum import IntEnum
from typing import List
import matplotlib.pyplot as plt
import networkx as nx
from IPython.display import display, Math

class LayerType(IntEnum):
    INPUT = 1
    HIDDEN = 2
    OUTPUT = 3
	
class ActivationFuncton(IntEnum):
	NONE = 1
	LOGISTICAL = 2

	
import numpy as np
def logistic(val):
	return 1 / (1 + np.e ** (-val) )

def logistic_partial(x):
	return x * (1-x)


def get_activation_function(function: ActivationFuncton):
    if int(function) == int(ActivationFuncton.LOGISTICAL):
        return logistic
    
def get_pd_activation_function(function: ActivationFuncton):
    if int(function) == int(ActivationFuncton.LOGISTICAL):
        return logistic_partial
    
class NeuralNetwork():
    LEARNING_RATE = 0.5
    def __init__(self, num_input):
        self.hidden_layers: List[NeuronLayer] = []
        self.num_input = num_input
        self.output_layer: NeuronLayer = None
        self.total_weights = 0
          
    def add_output_layer(self, num_neurons: Number, function: ActivationFuncton, weights=None, bias=None):
        layer = NeuronLayer(num_neurons, function, bias)
        previous_nodes = self.num_input

        if len(self.hidden_layers) > 0:
            previous_nodes = self.hidden_layers[-1].num_neurons

        i = 0
        for j in range(previous_nodes):
            for _ in range(num_neurons):
                weight = random.random()

                if len(weights) > i:
                    weight = weights[i]

                layer.neurons[j].weights.append(weight)
                i += 1

        self.output_layer = layer
        self.total_weights += i
		
    def add_hidden_layer(self, num_neurons: Number, function: ActivationFuncton, weights=None, bias=None):
        layer = NeuronLayer(num_neurons, function, bias)
        previous_nodes = self.num_input

        if len(self.hidden_layers) > 0:
            previous_nodes = self.hidden_layers[-1].num_neurons
            
        i = 0
        for j in range(previous_nodes):
            for _ in range(num_neurons):
                weight = random.random()

                if len(weights) > i:
                    weight = weights[i]

                layer.neurons[j].weights.append(weight)
                i += 1
        self.total_weights += i

        self.hidden_layers.append(layer)


    def visualize(self):
        G = nx.DiGraph()

        layer_positions = {}
        node_label_dict = {}
        edge_label_dict = {}
        edge_label_pos = {}

        # Initialize input layer nodes
        input_layer_nodes = [f"Input Layer_Neuron{i}" for i in range(self.num_input)]
        for i, node_name in enumerate(input_layer_nodes):
            G.add_node(node_name)
            layer_positions[node_name] = (0, -i)  # Position for input nodes
            node_label_dict[node_name] = f"i_{i}"  # Label for input nodes

        # Add hidden layers to the graph
        prev_layer_nodes = input_layer_nodes
        for i, layer in enumerate(self.hidden_layers, start=1):
            layer_name = f"Hidden Layer {i-1}"
            current_layer_nodes = []
            for j, neuron in enumerate(layer.neurons):
                node_name = f"{layer_name}_Neuron{j}"
                current_layer_nodes.append(node_name)
                G.add_node(node_name)
                layer_positions[node_name] = (i, -j)
                node_label_dict[node_name] = round(neuron.bias, 2)

                
                for k, prev_node in enumerate(prev_layer_nodes):
                    weight = neuron.weights[k]
                    G.add_edge(prev_node, node_name)
                    edge_label_dict[(prev_node, node_name)] = round(weight, 2)

            prev_layer_nodes = current_layer_nodes


        # Prepare output layer nodes separately to color them differently
        output_layer_nodes = []
        layer_name = "Output Layer"
        for j, neuron in enumerate(self.output_layer.neurons):
            node_name = f"{layer_name}_Neuron{j}"
            output_layer_nodes.append(node_name)
            G.add_node(node_name)
            layer_positions[node_name] = (len(self.hidden_layers) + 1, -j)
            node_label_dict[node_name] = round(neuron.bias, 2)

            for k, prev_node in enumerate(prev_layer_nodes):
                weight = neuron.weights[k]
                G.add_edge(prev_node, node_name)
                edge_label_dict[(prev_node, node_name)] = weight

        # Function to calculate edge label position (near the target node)
        def edge_label_position(source, target, offset):
            x0, y0 = layer_positions[source]
            x1, y1 = layer_positions[target]
            
            return (
                    x1 * offset + x0 * (1 - offset),
                    y1 * offset + y0 * (1 - offset)
                )

        new_edge_label_dict = {}
        # Calculate positions for edge labels
        for edge in G.edges():
            source, target = edge  # Unpack the edge tuple into source and target
            if source in layer_positions and target in layer_positions:
                edge_label_pos[source] = edge_label_position(source, target, 0)
                edge_label_pos[target] = edge_label_position(source, target, 1)
                new_edge_label_dict[edge] = edge_label_dict[edge]


        # Draw the graph
        plt.figure(figsize=(12, 4))
        # Draw input layer in green
        nx.draw(G, pos=layer_positions, nodelist=input_layer_nodes, 
                with_labels=True, labels=node_label_dict, node_size=3000, node_color='lightgreen')
        # Draw hidden layers in skyblue
        nx.draw(G, pos=layer_positions, nodelist=set(G.nodes()) - set(output_layer_nodes) - set(input_layer_nodes), 
                with_labels=True, labels=node_label_dict, node_size=3000, node_color='skyblue')
        # Draw output layer in orange
        nx.draw(G, pos=layer_positions, nodelist=output_layer_nodes, 
                with_labels=False, node_size=3000, node_color='orange')
        # Draw edge labels near the target nodes


        nx.draw_networkx_edge_labels(G,
                                     pos=edge_label_pos,
                                     edge_labels=new_edge_label_dict,
                                     label_pos=0.25)
        plt.title("Neural Network Visualization")
        plt.show()

    def feed_forward(self, inputs):
        nets = []
        outs = []
        if len(inputs) != self.num_input:
            raise ValueError("number of inputs must be equal to num_inputs")
        
        for layer in self.hidden_layers:
            net, outputs = layer.feed_forward(inputs)
            inputs = outputs

            nets.append(net)
            outs.append(outputs)

        net, outputs = self.output_layer.feed_forward(inputs)
        nets.append(net)
        outs.append(outputs)
        return nets, outs
    
    def get_weight(self, index):
        i = 0
        for layer in self.hidden_layers:
            for neuron in layer.neurons:
                for w in neuron.weights:
                    if i == index:
                        return w
                    
                    i += 1

        for neuron in self.output_layer.neurons:
            for w in neuron.weights:
                if i == index:
                    return w
                
                i += 1

        return None
    
    def train(self, training_inputs, training_outputs):

        new_network_weights = []
        nets = [[]]
        outs = [training_inputs]
        
        nets_, outs_ = self.feed_forward(training_inputs)
        nets.extend(nets_)
        outs.extend(outs_)


        print ("pd(z) => Partial Derative of z, in this case logistic function and so on")
        print ("out_n / net_n => w_n")
        print ("outputs per neuron (forward feed)", outs)

        outs_output = outs[-1]
        outs_last_hidden = outs[-2]
        
        # pd output activation func
        pd_out_func = get_pd_activation_function(self.output_layer.function)
        new_output_weight = []
        

        output_weight_count = self.total_weights - self.output_layer.num_neurons * len(self.output_layer.neurons[0].weights) + 1
        print("---------------")
        print ("1. Calculating new weights for output layer, DO NOT CHANGE THEM YET")


        new_layer_weights = []
        for i, out_o in enumerate(outs_output):
            for j, out_h in enumerate(outs_last_hidden):
                
                pd_total_output_weight = -(training_outputs[i] - out_o) * pd_out_func(out_o) * out_h
                new_weight = self.output_layer.neurons[i].weights[j] - NeuralNetwork.LEARNING_RATE * pd_total_output_weight
                new_output_weight.append(new_weight)
                print ()
                print ("\t",f"Calculating new value of w{output_weight_count}")
                print ("\t",f"∂E_total/∂w{output_weight_count}=-(y{i+1} - out_o{i+1}) * pd(g(out_o{i+1})) * out_h{j+1})", f",g={str(self.output_layer.function).replace('ActivationFuncton.', '')}")
                print ("\t",f"∂E_total/∂w{output_weight_count}=-({training_outputs[i]} - {out_o}) * {pd_out_func(out_o)} * {out_h}")
                print ("\t",f"w{output_weight_count}=w{output_weight_count}-α * ∂E_total/∂w{output_weight_count}")
                print ("\t",f"w{output_weight_count}={self.output_layer.neurons[i].weights[j]} - {NeuralNetwork.LEARNING_RATE} * {pd_total_output_weight}")
                print ("\t",f"w{output_weight_count}={new_weight}")

                output_weight_count += 1

                new_layer_weights.append(new_weight)

        new_network_weights.append(new_layer_weights)
                

        last_layer = self.output_layer
        processed_weight_count = self.output_layer.num_neurons * len(self.output_layer.neurons[0].weights)
        weights_left = self.total_weights - processed_weight_count

        layer_index = 2
        output_errors = [
            -(training_outputs[i] - outs[-1][i]) for i in range(len(training_outputs))
        ]
        print("---------------")
        
        for i, layer in enumerate(self.hidden_layers):

            new_layer_weights = []
            layer_weights = layer.num_neurons * last_layer.num_neurons
            start_weight = weights_left - layer_weights

            print (f"{i+2}. Calculating new weights for Hidden layer {len(self.hidden_layers)-i} , DO NOT CHANGE THEM YET")
            print (f"Therefore updating weights ({start_weight+1}-{start_weight+layer_weights})")

            outs_prev = outs[-(layer_index+1)]
            outs_this = outs[-layer_index]
            nets_this = nets[-layer_index]
            outs_next = outs[-(layer_index-1)]
            nets_next = nets[-(layer_index-1)]

            wi = 0
            output_wi_counter = weights_left
            for ni, neuron in enumerate(layer.neurons):
                weight_index = start_weight+wi
                print ("\t", f"Calculate w{weight_index}")

                expression =rf"""
                             \frac{{\partial{{E_{{total}}}}}}{{\partial{{w_{weight_index+1}}}}}=
                             \frac{{\partial{{E_{{total}}}}}}{{\partial{{out_{{h{i+1}{ni+1}}}}}}} *
                             \frac{{\partial{{out_{{h{i+1}{ni+1}}}}}}}{{\partial{{net_{{h{i+1}{ni+1}}}}}}} *
                             \frac{{\partial{{net_{{h{i+1}{ni+1}}}}}}}{{\partial{{w_{{{weight_index+1}}}}}}}
                             \\\\"""
                
                expression += rf"\frac{{\partial{{E_{{total}}}}}}{{\partial{{w_{weight_index+1}}}}}=("
                for oi in range(self.output_layer.num_neurons):
                    expression +=  rf"\frac{{\partial{{E_{{o{oi+1}}}}}}}{{\partial{{out_{{h{i+1}{ni+1}}}}}}}+"

                expression = expression[:-1]
                expression += ")"
                expression += rf"""
                *
                \frac{{\partial{{out_{{h{i+1}{ni+1}}}}}}}{{\partial{{net_{{h{i+1}{ni+1}}}}}}} *
                \frac{{\partial{{net_{{h{i+1}{ni+1}}}}}}}{{\partial{{w_{{{weight_index+1}}}}}}}
                \\\\
                """


                
                expression += rf"\frac{{\partial{{E_{{total}}}}}}{{\partial{{w_{weight_index+1}}}}}=(("
                for oi in range(self.output_layer.num_neurons):
                    expression += rf"\frac{{\partial{{E_{{o{oi+1}}}}}}}{{\partial{{net_{{o{i+1}{ni+1}}}}}}} *"
                    expression += rf"\frac{{\partial{{net_{{o{oi+1}}}}}}}{{\partial{{out_{{h{i+1}{ni+1}}}}}}}"
                    expression += ")+("

                expression = expression[:-2]

                expression += rf"""
                )*
                \frac{{\partial{{out_{{h{i+1}{ni+1}}}}}}}{{\partial{{net_{{h{i+1}{ni+1}}}}}}} *
                \frac{{\partial{{net_{{h{i+1}{ni+1}}}}}}}{{\partial{{w_{{{weight_index+1}}}}}}}
                """

                expression += rf"=(("

                # CALCULATE the error values
                p1 = 0
                p2 = 0
                p3 = 0
                for oi in range(self.output_layer.num_neurons):
                    
                    expression += rf"\frac{{\partial{{E_{{o{oi+1}}}}}}}{{\partial{{net_{{o{i+1}{ni+1}}}}}}} *"
                    expression += rf"w_{{{output_wi_counter}}}"

                    pd_E_net__pd_net = output_errors[oi] * get_pd_activation_function(layer.function)(outs_next[oi])

                    
                    eq = pd_E_net__pd_net * self.get_weight(output_wi_counter)

                    p1 += eq
                    expression += ")+("

                    output_wi_counter += 1

                expression = expression[:-2]


                
                expression += rf")* \partial{{g(out_{{h{i+1}{ni+1}}})}} *"
                expression += rf"out_{{h{i+1}{ni+1}}}"
                
                p2 = get_pd_activation_function(layer.function)(outs_this[ni])
                p3 = outs_prev[ni]
                values_multiplied = p1 *p2*p3
                expression += f"\\\\={p1} * {p2} * {p3} = {values_multiplied}"

                display(Math(expression))

                new_weight = self.get_weight(weight_index) - NeuralNetwork.LEARNING_RATE *values_multiplied

                wi += 1

                new_layer_weights.append(new_weight)

            new_network_weights.insert(0, new_layer_weights)

        print (new_network_weights)

                



class NeuronLayer:
    def __init__(self, num_neurons, function: ActivationFuncton, bias):

        self.function = function
        self.num_neurons = int(num_neurons)
        # Every neuron in a layer shares the same bias
        self.bias = bias if bias else random.random()

        self.neurons = []
        for i in range(num_neurons):
            self.neurons.append(Neuron(self.bias))

    def inspect(self):
        print('Neurons:', len(self.neurons))
        for n in range(len(self.neurons)):
            print(' Neuron', n)
            for w in range(len(self.neurons[n].weights)):
                print('  Weight:', self.neurons[n].weights[w])
            print('  Bias:', self.bias)

    def feed_forward(self, inputs):
        nets = []
        outs = []
            
        net = 0

        for neuron in self.neurons:
            net = self.bias


            for i, input in enumerate(inputs):
                net += neuron.weights[i] * input

            nets.append(net)
            outs.append(get_activation_function(self.function)(net))
        
        return nets, outs

    def get_outputs(self):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.output)
        return outputs
    

class Neuron:
    def __init__(self, bias):
        self.bias = bias
        self.weights = []

    def calculate_output(self, inputs, function):
        self.inputs = inputs
        nets = self.calculate_total_net_input()
        outs = function(nets)

        self.output =  outs
        return (nets, outs)

    def calculate_total_net_input(self):
        total = 0

        
        for i in range(len(self.inputs)):
            total += self.inputs[i] * self.weights[i]
        return total + self.bias

    # Apply the logistic function to squash the output of the neuron
    # The result is sometimes referred to as 'net' [2] or 'net' [1]
    def squash(self, total_net_input):
        return 1 / (1 + math.exp(-total_net_input))

    # Determine how much the neuron's total input has to change to move closer to the expected output
    #
    # Now that we have the partial derivative of the error with respect to the output (∂E/∂yⱼ) and
    # the derivative of the output with respect to the total net input (dyⱼ/dzⱼ) we can calculate
    # the partial derivative of the error with respect to the total net input.
    # This value is also known as the delta (δ) [1]
    # δ = ∂E/∂zⱼ = ∂E/∂yⱼ * dyⱼ/dzⱼ
    #

    def calc_delta_rule(self, target_output, pd_activation_function):
        return self.calculate_pd_error_wrt_output(target_output) * pd_activation_function(self.output)

    # The error for each neuron is calculated by the Mean Square Error method:
    def calculate_error(self, target_output):
        return 0.5 * (target_output - self.output) ** 2

    # The partial derivate of the error with respect to actual output then is calculated by:
    # = 2 * 0.5 * (target output - actual output) ^ (2 - 1) * -1
    # = -(target output - actual output)
    #
    # The Wikipedia article on backpropagation [1] simplifies to the following, but most other learning material does not [2]
    # = actual output - target output
    #
    # Alternative, you can use (target - output), but then need to add it during backpropagation [3]
    #
    # Note that the actual output of the output neuron is often written as yⱼ and target output as tⱼ so:
    # = ∂E/∂yⱼ = -(tⱼ - yⱼ)
    def calculate_pd_error_wrt_output(self, target_output):
        return -(target_output - self.output)


    # The total net input is the weighted sum of all the inputs to the neuron and their respective weights:
    # = zⱼ = netⱼ = x₁w₁ + x₂w₂ ...
    #
    # The partial derivative of the total net input with respective to a given weight (with everything else held constant) then is:
    # = ∂zⱼ/∂wᵢ = some constant + 1 * xᵢw₁^(1-0) + some constant ... = xᵢ
    def calculate_pd_total_net_input_wrt_weight(self, index):
        return self.inputs[index]

	