(function () {
	const pyenv = document.createElement("py-env");
  
  let modules = ["numpy", "requests", "matplotlib"];
  
  for (var i = 0; i < modules.length; ++i) {
    modules[i] = '- '+modules[i];
  }
  modules = [""].concat(modules)
  modules.push("");
  let content = modules.join('\r\n')
  
  pyenv.innerHTML = content;
	document.head.appendChild(pyenv);
 
})();