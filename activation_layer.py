#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:16:52 2020

@author: milan
"""

from layer import Layer

#inherit from base class
class ActivationLayer(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime
        
    #return the activation input
    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = self.activation(self.input)
        return(self.output)
    
    #return input_error = dE/dX for a given output_error=dE/dY
    def backward_propagation(self, output_error, learning_rate):
        return(self.activation_prime(self.input) * output_error)