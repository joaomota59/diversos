class Layer(object):
    def setInputShape(self, shape):
        """ 
        Define o shape que a camada espera e que será usada 
        no método forwardPass.
        """
        self.input_shape = shape
    
    def layerName(self):
        """ 
        Define o nome da camada. 
        Usado no sumário da rede. 
        """
        return self.__class__.__name__
    
    def parameters(self):
        """ 
        Define o número de parâmetros usados na camada 
        """
        return 0
    
    def forwardPass(self, X, training):
        """ 
        Método que realiza a propagação do treinamento para frente (forward).
        """
        raise NotImplementedError()
    
    def backwardPass(self, accumulated_gradient):
        """
        Parametros:
        accumutated_gradient: gradiente acumulado da camada de saída.
        
        Descrição:
        Método que propaga o gradiente acumulado para trás (backward).
        Se houver pesos treináveis, eles serão atualizados.
        
        Retorno: retorna o gradiente em relação a saída da camada anterior.
        """
        raise NotImplementedError()
    
    def outputShape(self):
        raise NotImplementedError()