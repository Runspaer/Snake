from obj import *
import math as m
class Snake(Circle):
    def __init__(self,coord:Point,vel:Point,color,r:int,tail:list):
        super().__init__(coord,vel,color,r)
        self.tail=tail#Circle

    def tick(self):
        pass
        # for i in range(1,len(self.tail)):
        #     self.tail[-i].glv=self.tail[-i-1].glv.copy()
        #     self.tail[-i].locv = self.tail[-i - 1].locv.copy()
        #     self.tail[-i].size = self.tail[-i - 1].size.copy()
        # if self.tail:
        #     self.tail[0].glv = self.vec.glv.copy()
        #     self.tail[0].locv = self.vec.locv.copy()
        #     self.tail[0].size = self.vec.size.copy()
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_RIGHT]:
        #     self.vec.locv=np.dot(np.array([[m.cos(m.radians(5)),-m.sin(m.radians(5))],[m.sin(m.radians(5)),m.cos(m.radians(5))]],float),self.vec.locv)
        #
        # if keys[pygame.K_LEFT]:
        #     self.vec.locv = np.dot(np.array([[m.cos(m.radians(5)),m.sin(m.radians(5))], [-m.sin(m.radians(5)), m.cos(m.radians(5))]],float),self.vec.locv)
        #
        # self.vec.glv = self.vec.new_glcd()