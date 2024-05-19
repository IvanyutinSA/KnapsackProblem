import matplotlib.pyplot as plt
from algorithm.genetic import Genetic
from tests.randomtests import Tests

class Visual:  
    def Grafik(self, knapsacks, capacities, otvet):
        plt.figure(figsize=(10, 5))
        indexs=range(1, len(knapsacks)+1)
        alg_res= []
        for knapsack, capacity in zip( knapsacks, capacities):
            genetic = Genetic()
            alg_res.append(  genetic.solve(knapsack, capacity)[0] )
            # print( alg_res[-1] )
        plt.plot(indexs, alg_res, marker='o', color='red')
        plt.plot(indexs, otvet, marker='o', color='green')
        plt.ylabel('Стоймость взятых вещей')
        plt.xlabel('Номер рюкзака')
        plt.show()
        print()
    
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

    def Otklonenie(self, genetic_results, lib_results):
        nomer=1
        sovpalo=0
        errors = []
        for genetic, lib in zip( genetic_results, lib_results):
            # print(genetic, lib)
            if genetic == lib:
                sovpalo+=1
                errors.append(100)
            else:
                # наш на библиотечный вариант
                true_proc = round( genetic / lib * 100, 2)
                errors.append(true_proc)
            nomer+=1
        plt.plot( range(3, nomer+2) , errors, marker='o', linestyle='-' ,label="errors" ,color='red')
        plt.ylabel('Процент совпадения')
        plt.xlabel('Количество вещей в рюкзаке')
        plt.show()
        

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
        self.Otklonenie(genetic_results, lib_results)
        # вывод графика
        plt.plot(rand_indexs, genetic_results, marker='o', label="genetic_results" ,color='blue')
        plt.plot(rand_indexs, lib_results, marker='o', linestyle='--' ,label="lib_results" ,color='green')
        plt.ylabel('Стоймость взятых вещей')
        plt.xlabel('Количество вещей в рюкзаке')
        plt.legend()
        plt.show()
        print()