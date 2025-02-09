import random
class network():
    def __init__(self,layerinfo,build_type = "n"): #Makes New or uploads old network
        self.layers = []
        self.length = len(layerinfo)
        if build_type.lower() == "n":
            self.__makenewnetwork(layerinfo)
        else:
            self.__loadnetwork(layerinfo)

    def __makenewnetwork(self,layerinfo):#Part of init.
        for i in range(len(layerinfo)):
                layercount = layerinfo[i] 
                if not i == 0:
                    pre_layer = layerinfo[i-1]
                else:
                    pre_layer = 0

                layer = [neuron(pre_layer) for _ in range(layercount)]
                self.layers.append(layer)
    def __loadnetwork(self,layerinfo):#Part of init
        layerslist = []
        for layer in layerinfo:
            layerlist = []
            for item in layer:
                weights = item[0]
                bias = item[1]
                layerlist.append(neuron(weights,bias))
            layerslist.append(layerlist)
        self.layers = layerslist

    def getdata(self):#Puts all of the networks weights and biases into a tuple
        returnlayers = []
        for layer in self.layers:
            templayer = []
            for neuron in layer:
                templayer.append(neuron.getdata())
            returnlayers.append(templayer)
        return tuple(returnlayers)

    def run(self,inputdata):#Runs network returns output neurons values in a tuple
        datavector = inputdata
        for i in range(1, self.length):
            layer = self.layers[i]
            layerdata = []
            
            for neuron in layer:
                data = neuron.run(datavector)
                layerdata.append(data)

            datavector = layerdata

        return tuple(datavector)

    def vary(self, weightvary, biasvary):#Adds random vary to all baises and weights
        for layer in self.layers:
            for neuron in layer:
                neuron.vary_bias(biasvary)
                neuron.vary_weights(weightvary)

class neuron():
    def __init__(self,weights,bias = 0):#Sets up the neuron
        self.bias = bias
        if type(weights) == int:
            self.weights = [0 for _ in range(weights)]
        else:
            self.weights = weights

    def run(self, inputvector):#Puts vector into a neuron and gets an output (Between 0 and 1)
        item = self.__dotproduct(inputvector, self.weights)
        return self.__squash(item+self.bias)

    def getdata(self):#Gets weights and bias of a neuron
        return (self.weights, self.bias)
    
    def __squash(self,item): #Returns item as point on sigmoid graph (In other words squeezes down real numberline between 0 and 1) 
        returnitem = (1/(1+(2.71828**-item)))
        return returnitem
    def __dotproduct(self, item1, item2): #Returns Dotproduct of 2 inputed values
        vector = self.__multiplyvectors(item1,item2)
        returnint = self.__addup(vector)
        return returnint
    def __multiplyvectors(self, item1, item2): #Times two arrays together. Returns tuple of answer
        returnvector = []
        for i in range(len(item1)):
            returnvector.append(item1[i]*item2[i])
        return tuple(returnvector)
    def __addup(self,item): #Adds up all items in array into one number
        returnint = 0
        for i in item:
            returnint += i
        return returnint
    
    def vary_bias(self, item):# Adds an adjustment to bias between 2 input values
        item1, item2 = item
        adjust = self.__get_float_between(item1,item2)
        self.bias += adjust
    def set_bias(self,bias):
        self.bias = bias
    def get_bias(self):
        return self.bias

    def vary_weights(self, item):# Adds an adjustment to weights between 2 input values (Changes per item in the weights)
        item1,item2 = item
        weightlist = []
        for i in range(len(self.weights)):
            adjusted_value = self.weights[i] + self.__get_float_between(item1, item2)
            weightlist.append(adjusted_value)
        self.weights = tuple(weightlist)
    def set_weights(self, weights):
        self.weights = weights
    def get_weights(self):
        return self.weights

    def __get_float_between(self,item1,item2):#Gets a float between 2 inputed values
        return random.uniform(item1,item2)
    
s = network((2,100,2))
input = (-1,1)
for _ in range(100):
    input = s.run(input)
    print(input)
    s.vary((-0.01,0.01),(-0.01,0.01))
