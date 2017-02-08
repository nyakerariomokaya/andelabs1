class Car(object):
    def __init__(self, name='General', model='GM', car_type='saloon', num_of_doors=4, num_of_wheels=4, speed=0):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels
        self.speed = speed
       

        if self.name =='Porshe' or self.name == 'Koenigsegg':
           self.num_of_doors = 2
        else:
           self.num_of_doors = 4
    
        if self.car_type =='trailer':
           self.num_of_wheels=8
                   
                
    def is_saloon(self):
          if self.car_type !='trailer':
             return True   
          return False
         
    def drive(self, moving_speed):
          if moving_speed ==3:
             self.speed=1000
          elif moving_speed==7:
              self.speed=77
          return self

                  

            
             
