import matplotlib.pyplot as plt
import numpy as np
from algorithm.genetic import Genetic
from tests.randomtests import Tests

class Visual:  
    def ResultPlot(self, y_hat, y):
        plt.figure(figsize=(10, 5))
        indexes = np.array(range(1, len(y)+1))
        plt.plot(indexes, y_hat, marker='o', color='#136970', label='реализованный')
        plt.plot(indexes, y, marker='o', color='green', label='библиотечный')
        plt.ylabel('Значения')
        plt.xlabel('Номер попытки') 
        plt.title('Сравнение результатов')
        
        plt.legend()
        plt.show()

    def MatchPlot(self, y_hat, y):
        plt.figure(figsize=(10, 5))
        indexes = list(range(1, len(y)+1))
        plt.plot(indexes, np.array(y_hat)/np.array(y)*100, marker='o', color='green')
        plt.ylabel('Процент совпадения')
        plt.xlabel('Номер попытки')
        plt.title('Сравнение в соотношении')
        plt.show()

    def Grafik(self, knapsacks, capacities):
        plt.figure(figsize=(10, 5))
        indexs=range(1, len(knapsacks)+1)
        alg_res= []
        for knapsack, capacity in zip( knapsacks, capacities):
            genetic = Genetic()
            alg_res.append(  genetic.solve(knapsack, capacity)[0] )
            # print( alg_res[-1] )
        plt.plot(indexs, alg_res, marker='o', color='#136970')
        plt.ylabel('Стоймость взятых вещей')
        plt.xlabel('Номер рюкзака')
        plt.show()
    
    def Sovpadenia(self, genetic_results, lib_results):
        nomer=1
        sovpalo=0
        for genetic, lib in zip( genetic_results, lib_results):
            # print(genetic, lib)
            if genetic == lib:
                print( nomer,'полностью совпало' )
                sovpalo+=1
            else:
                # разница на библиотечный вариант
                error = round(abs(genetic-lib) / lib * 100, 2)
                print(nomer, 'не совпало на', error, '%' )
            nomer+=1
        # процент полного совпадения
        print('\nПолностью совпало:', round(sovpalo/(nomer-1)*100, 2) , '%' )

    def RandomTest_Grafik(self, items: int = 3 ):
        plt.figure(figsize=(10, 5))
        # масс с кол вещ в рюкзаке (их мин 3)
        rand_indexs=range(3, items+3)
        genetic_results, lib_results = [], [];
        # записываем результаты
        for i in rand_indexs:
            t = Tests()
            r_knapsack, r_capacity, genetic_result, lib_result = t.Random(items=i)
            genetic_results.append(genetic_result[0])
            lib_results.append(lib_result[0])
        # проверка совпадения
        self.Sovpadenia(genetic_results, lib_results)
        # вывод графика
        plt.plot(rand_indexs, genetic_results, marker='o', label="genetic_results" ,color='blue')
        plt.plot(rand_indexs, lib_results, marker='o', linestyle='--' ,label="lib_results" ,color='green')
        plt.ylabel('Стоимость взятых вещей')
        plt.xlabel('Количество вещей в рюкзаке')
        plt.legend()
        plt.show()
        print()
    
    def Time_Grafik(self, genetic_time, lib_time):
        plt.figure(figsize=(10, 5))
        indexes = np.array(range(1, len(lib_time)+1))
        genetic_time = [round(np.mean([g for g in genetic_time if g > 0])) if g < 0 else g for g in genetic_time ]
        plt.plot(indexes, genetic_time, marker='o', color='#136970', label='реализованный')
        plt.plot(indexes, lib_time, marker='o', color='green', label='библиотечный')
        plt.ylabel('Время (мкс)')
        plt.xlabel('Номер попытки')
        plt.title('Время выполнения')
        plt.legend()

        plt.show()
    
    def Time_Grafik_Math(self, genetic_time, lib_time):
        plt.figure(figsize=(10, 5))
        indexes = list(range(1, len(lib_time)+1))
        values=list(zip(genetic_time, lib_time))
        times_procent= []  
        all_time_gen, all_time_lib=0,0
        for value in values:
            all_time_gen+=value[0]
            all_time_lib+=value[1]
            time_procent= min(value)/max(value)*100
            times_procent.append(time_procent)
        plt.plot(indexes, times_procent, marker='o', color='#136970')
        plt.ylabel('Процент разницы')
        plt.xlabel('Номер задачи')
        plt.title('График процента разницы в выполнении')
        plt.show()
        #круговая диаграмма
        plt.pie([all_time_gen, all_time_lib],
                labels=[f"Генетический-{round(all_time_gen,1)}",f"Библиотечный-{round(all_time_lib,1)}"],
                autopct='%1.1f%%')
        plt.title("Соотношение времени выпонения алгоритмов")
        plt.show()
