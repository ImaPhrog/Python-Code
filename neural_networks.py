import random
class network():
    def __init__(self,layerinfo):
        self.layers = []
        for layersize in layerinfo:
            self.layers.append(layer(layersize))


class layer():
    def __init__(self, count):#Sets up the object to store groups of neuron (amount based on input)
        self.neurons = [neuron() for _ in range(count)]
    def run(self, inputvector):#Sends all the inputs for the layer into each neuron in the layer
        returnvector = []
        for neuron in self.neurons:
            returnvector.append(neuron.run(inputvector))
        return tuple(returnvector)

    def adjust_neurons_biases(self, item1, item2):#Adjusts each neurons baiases between 2 inputed numbers
        for neuron in self.neurons:
            neuron.adjust_bias(item1,item2)
    def adjust_neurons_weights(self,item1,item2):#Adjusts each neurons weights between 2 inputed numbers
        for neuron in self.neurons:
            neuron.adjust_weights(item1,item2)

class neuron():
    def __init__(self,wieghts,bias = 0):#Sets up the neuron
        # self.weights = 
        self.bias = bias

    def run(self, inputvector):#Puts vector into a neuron and gets an output (Between 0 and 1)
        item = self.__dotproduct(inputvector, self.weights)
        return self.__squash(item+self.bias)




        return random.uniform(item1,item2)

    def __squash(self,item): #Returns item as point on sigmoid graph (In other words squeezes down real numberline between 0 and 1) 
        returnitem = (1/(1+(2.7**-item)))
        return returnitem
    def __dotproduct(self, item1, item2): #Returns Dotproduct of 2 inputed values
        vector = self.__multiplyvectors(item1,item2)
        returnint = self.__addup(vector)
        return returnint
    def __multiplyvectors(self, item1, item2): #Times two (lists / tuples) together. Returns tuple of answer
        returnvector = []
        for i in range(len(item1)):
            returnvector.append(item1[i]*item2[i])
        return tuple(returnvector)
    def __addup(self,item): #Adds up all items in (list / tuple) into one number
        returnint = int
        for i in item:
            returnint += i
        return returnint
    
    def adjust_bias(self, item1, item2):# Adds an adjustment to bias between 2 input values
        adjust = self.__get_float_between(item1,item2)
        self.bias += adjust
    def adjust_weights(self, item1, item2):# Adds an adjustment to weights between 2 input values (Changes per item in the weights)
        weightlist = []
        for i in range(self.weights):
            adjusted_value = self.weights[i] + self.__get_float_between(item1, item2)
            weightlist.append(adjusted_value)
        self.weights = tuple(list)
        self.weights = item
    def __get_float_between(self,item1,item2):#Gets a float between 2 inputed values
        return random.uniform(item1,item2)
    
#Do network (Group of networks)
#Do layers (Group of neurons)
#Figure out weights for neurons (Do it based on amount of neurons in layer before)

#Make method to return information about network and input method to allow for direct varible setting