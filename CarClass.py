class Car(object):
      def __init__(self,name="General",model="GM",car_type="saloon",num_of_doors=4,num_of_wheels=4,speed=0):
          self.name=name
          self.model=model
          self.car_type = car_type
          self.no_of_doors=4
          self.no_of_wheels=4

          if self.name =='Porshe' or 'Koenigsegg':
             self.num_of_doors = 2
          else:
             self.num_of_doors=4
     
          if self.car_type =='trailer':
             self.num_of_wheels=8
          else:
             self.num_of_wheels=4           
                
      def is_saloon(self):
          if self.car_type !='trailer':
             self.car_type =='saloon'
             return True   
         
      def drive(self, moving_speed):
          if moving_speed ==1000:
             self.speed=3
          elif moving_speed==77:
              self.speed=7
              return self

                  

            
             
