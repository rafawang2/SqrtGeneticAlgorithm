import random
import math
POPULATION = 100    #初始族群大小
MUTATION_RATE = 0.05  #突變率
END_CONDITION = 1e-20
END_GENERATION = 10000

class GeneSqrt():
    def __init__(self,n) -> None:
        self.n = n
        
    #生成初始族群
    def GenerateInitialGroup(self):
        if self.n > 4:  #n>4時，n平方弊大於2n，為加快速度選擇0~n/2的範圍去生成族群
            return [random.uniform(0, self.n // 2) for i in range(POPULATION)]
        else:
            return [random.uniform(0, self.n) for i in range(POPULATION)]
    
    #適應函數，x平方與n的差距越小越好
    def fitness(self,x):
        return -abs(x**2-self.n)
    
    #選擇
    def selection(self, generation):
        #從當前世代族群隨機選兩個不重複的
        selected = random.sample(generation, 2)
        return max(selected, key=self.fitness)  #回傳適應值最大的基因
    
    def cross(self,father, mother):    
        Proportion = random.random()    #子代佔比差異(0~1之間)
        #交配
        child1 = (1-Proportion) * father + Proportion * mother
        child2 = (1-Proportion) * mother + Proportion * father
        return child1, child2
    
    def mutate(self,x):
        if random.random() < MUTATION_RATE:
            x += random.uniform(-1, 1)  #小幅度改變x，突變範圍-1~1
        return x
    
    def simulate_start(self):
        generation = self.GenerateInitialGroup()
        best_gene = self.n+1
        gen_cnt = 1
        while(abs(best_gene**2 - self.n) > END_CONDITION and not (gen_cnt > END_GENERATION)):
            new_generation = []
            for i in range(POPULATION//2):  #一次交配產生兩個後代，故只需要重複族群數的一辦次數
                father = self.selection(generation=generation)
                mother = self.selection(generation=generation)
                child1, child2 = self.cross(father=father, mother=mother)
                child1 = self.mutate(x=child1)
                child2 = self.mutate(x=child2)
                new_generation.append(child1)
                new_generation.append(child2)
            generation = new_generation
            
            #找到目前最好的基因
            best_gene = max(generation, key=self.fitness)
            best_fitness = self.fitness(best_gene)
            print(f"第{gen_cnt}代： 最佳解->{best_gene}，適應值->{best_fitness}")
            gen_cnt+=1


n = int(input())
Ans = GeneSqrt(n)
Ans.simulate_start()
print(f"正確解答：{math.sqrt(n)}")