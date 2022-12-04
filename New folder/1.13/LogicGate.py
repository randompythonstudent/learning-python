class LogicGate:
    def __init__(self, lbl):
        self.label = lbl
        self.output = None
        
    def get_label(self):
        return self.label
    
    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output
    
class BinaryGate(LogicGate):
    def __init__(self,lbl):
        LogicGate.__init__(self, lbl)
        self.pin_a = None
        self. pin_b = None
    
    def get_pin_a(self):
        return int(input(f"Enter pin A input for gate \
            {self.get_label()}: "))
    
    def get_pin_b(self):
        return int(input(f"Enter pin B input for gate \
            {self.get_label()}: "))

class UnaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)
        self.pin = None
    def get_pin(self):
        return int(input(f"Enter pin input for gate \
            {self.get_label()}: "))
class AndGate(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
class OrGate(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0        
class NotGate(UnaryGate):
    def __init__(self, lbl):
        UnaryGate.__init__(self, lbl)
        
    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1   
class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)  
    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate     
def set_next_pin(self, source):
    if self.pin_a == None:
        self.pin_a = source
    else:
        if self.pin_b == None:
            self.pin_b == source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")
def get_pin_a(self):
    if self.pin_a == None:
        return input(
            f"Enter pin A input for gate \
                {self.get_label()}:"
                )
    else:
        return self.pin_a.get_from().get_output()")
# g1 = AndGate("G1")
# g1.get_output()
# g2 = OrGate("G2")
# g2.get_output()
# g3 = NotGate("G3")
# g3.get_output()
g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)