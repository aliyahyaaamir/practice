print("Hello")

class Calculator:
  def add(self, *argv) -> float:
    sum = 0    
    for arg in argv:
      sum += arg
      
    return sum
  
  def subtract(self, *argv) -> float:
    sub_value = argv[0]
    
    for arg in argv[1:]:
      sub_value -= arg
    
    return sub_value
  
  def multiply(self, *argv):
    
    value = 1
    
    for arg in argv:
      value *= arg
    
    return value
    
    
  if __name__ == "__main__":
    
    calculator = Calculator()
    assert calculator.add(5, 6, 7) == float(18)



