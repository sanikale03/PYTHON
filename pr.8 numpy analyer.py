
# =======================  PR.8 NUMPY ANALYZER  =========================

import numpy as np
print("welcome to the numpy analyzer!")
class create_array:
    def __init__(self):
        pass              
    
    # ================= ARRAY CREATION =================
    
     # ================= 1D array =================
    
    def create_1D(self):
        n=int(input("enter the numbers of elements"))
        elements = list(map(int, input(f"Enter {n} elements (space separated): ").split()))
        self.a1 = np.array(elements)
        print("\n1D Array:")
        print(self.a1)
        print("Shape:", self.a1.shape, "\n")
        self.index_slice_menu("1D")

     # ================= 2D array =================
 
    def create_2d_array(self):
        rows = int(input("Enter number of rows for 2D array: "))
        cols = int(input("Enter number of columns for 2D array: "))
        print(f"Enter {rows * cols} elements (space separated):")
        elements = list(map(int, input().split()))
        self.a2 = np.array(elements).reshape(rows, cols)
        print("\n2D Array:")
        print(self.a2)
        print("Shape:", self.a2.shape, "\n")
        self.index_slice_menu(self.a2,"2D")

     # ================= 3D array ===================
     
    def create_3d_array(self):
        d1 = int(input("Enter size for 1st dimension of 3D array: "))
        d2 = int(input("Enter size for 2nd dimension of 3D array: "))
        d3 = int(input("Enter size for 3rd dimension of 3D array: "))
        print(f"Enter {d1 * d2 * d3} elements (space separated):")
        elements = list(map(int, input().split()))
        self.a3 = np.array(elements).reshape(d1, d2, d3)
        print("\n3D Array:")
        print(self.a3)
        print("Shape:", self.a3.shape, "\n")
        
     # =================  INDEXING AND SLICING MENU   =================
     
        self.index_slice_menu(self.a3,"3D")
    def index_slice_menu(self,arr,arr_type):
        while True:
            print(f"\n {arr_type} Array Indexing & Slicing Menu ")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Exit to Main Menu")
            choice = int(input("Enter your choice: "))

            if arr_type == "1D":
                arr = self.a1
            elif arr_type == "2D":
                arr = self.a2
            else:
                arr = self.a3

     # ================= Indexing =================
   
            if choice == 1:  
                idx = tuple(map(int, input("Enter index/indices (space separated): ").split()))
                try:
                    print("Indexed Value:", arr[idx])
                except Exception as e:
                 print("⚠ Invalid index:", e)
                 
     # ================= Slicing =================
     
            elif choice == 2:  
                if arr_type == "1D":
                    s = slice(*[int(x) if x else None for x in input("Enter slice (start:end): ").split(":")])
                    print("Sliced Array:", arr[s])
                else:
                    print("Enter slices for each dimension separated by comma (ex: 0:2,1:3)")
                    slices = input("Slices: ")
                    slice_objs = tuple(
                        slice(int(x.split(":")[0]) if x.split(":")[0] else None,
                              int(x.split(":")[1]) if len(x.split(":")) > 1 and x.split(":")[1] else None)
                        for x in slices.split(",")
                    )
                    print("Sliced Array:\n", arr[slice_objs])
            elif choice == 3:
                break
            else:
                print("Invalid choice!")
ca=create_array()

# ================= MATHEMATICAL OPERATIONS ===================

class mathematical_operations:
    def __init__(self):
        self.arr1 = None
        self.arr2 = None

    def input_arrays(self):
        n = int(input("Enter number of elements for arrays: "))
        print(f"Enter {n} elements for first array:")
        elements1 = list(map(float, input().split()))
        print(f"Enter {n} elements for second array:")
        elements2 = list(map(float, input().split()))
        self.arr1 = np.array(elements1)
        self.arr2 = np.array(elements2)
        print("\nFirst Array:", self.arr1)
        print("Second Array:", self.arr2)
        
# ================= Add =================

    def add(self):
        print("\nAddition:", self.arr1 + self.arr2)

# ================= Subtract ===============

    def subtract(self):
        print("Subtraction:", self.arr1 - self.arr2)

# ================= Multiply =================

    def multiply(self):
        print("Multiplication:", self.arr1 * self.arr2)

# ================= Divide =================
    def divide(self):
        print("Division:", self.arr1 / self.arr2)
        
    def operations(self):
        self.input_arrays()
        self.add()
        self.subtract()
        self.multiply()
        self.divide()
mo=mathematical_operations()

# ================= COMBAIN AND SPLITES =================

class combine_split_arrays:
 def combine_arrays(self):
    n=int(input("enter the number of elements for the first array:"))
    elements1=list(map(int,input(f"enter{n} elements for the first array(space sperated): ") .split()))
    arr1=np.array(elements1)

    m=int(input("enter the number of elements for the second array:"))
    elements2=list(map(int,input(f"enter{m} elements for the second array(space sperated): ") .split()))
    arr2=np.array(elements2)
    print("\nFirst Array:", arr1)
    print("Second Array:", arr2)

    # ================= Combine arrays =================
    
    combined = np.concatenate((arr1, arr2))
    print("Combined Array:", combined)
 def split_array(self):
    n=int(input("enter the numbers of elements for the array:"))
    elements=list(map(int,input(f"enter {n} elements for the array(space seperated):").split()))
    arr=np.array(elements)
    print("\noriginal array:",arr)
    
    # ================= split array =================
    
    k = int(input("Enter how many parts you want to split the array into: "))
    try:
    # split only works if n is divisible by k
      splitted = np.split(arr, k)
    except ValueError:
    # if not divisible, use array_split
      splitted = np.array_split(arr, k)

    print("\nSplitted Arrays:")
    for i, part in enumerate(splitted, start=1):
     print(f"Part {i}:", part)
cs=combine_split_arrays()

# ================= SEARCH AND SORT AND FILTER =================

class search_sort_filter_arrays:
  def __init__(self):
       self.arr=None
  def input_array(self):
        dims = int(input("Enter dimensions of array (1, 2 or 3): "))
        if dims == 1:
            n = int(input("Enter number of elements: "))
            elements = list(map(int, input(f"Enter {n} elements (space separated): ").split()))
            self.arr = np.array(elements)
        elif dims == 2:
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))
            elements = list(map(int, input(f"Enter {r*c} elements (space separated): ").split()))
            self.arr = np.array(elements).reshape(r, c)
        elif dims == 3:
            x = int(input("Enter dimension 1: "))
            y = int(input("Enter dimension 2: "))
            z = int(input("Enter dimension 3: "))
            elements = list(map(int, input(f"Enter {x*y*z} elements (space separated): ").split()))
            self.arr = np.array(elements).reshape(x, y, z)
        else:
            print("Invalid dimension!")
            return
        print("\nOriginal Array:\n", self.arr)
        
 # ============ SEARCH ============
 
  def search(self):
    x = int(input("Enter element to search: "))
    indices = np.where(self.arr == x)
    if indices[0].size > 0:
        indices=list(zip(*indices))
        print(f"Element {x} found at index/indices: {indices}")
    else:
        print(f"Element {x} not found in the array.")

 # =========== SHORT =================
 
  def sort(self):
        sorted_arr = np.sort(self.arr)
        print("Sorted Array:", sorted_arr)

 # =========== FILTER  ================
 
  def filter(self):
        val = int(input("Enter a threshold value: "))
        filtered = self.arr[self.arr > val]
        print(f"Elements greater than {val}:", filtered)
  def operations(self):
       if self.arr is None:
        print("⚠ No array found. Please create one first!")
        self.input_array()
       while True:
            print("\n Search/Sort/Filter Menu ")
            print("1. Search")
            print("2. Sort")
            print("3. Filter")
            print("4. Exit")
            choice = int(input("Enter choice: "))
            if choice == 1: self.search()
            elif choice == 2: self.sort()
            elif choice == 3: self.filter()
            elif choice == 4: break
            else: print("Invalid choice!")
sa=search_sort_filter_arrays()

# =============== COMPUTE AGGREGATES STATICS  ===================

class compute_aggregates_statics:
     def __init__(self):
       self.arr=None
     def input_array(self):
        n = int(input("Enter number of elements for the array: "))
        elements = list(map(float, input(f"Enter {n} elements (space separated): ").split()))
        self.arr = np.array(elements)
        print("\nOriginal Array:", self.arr)

 # =========== aggregate  ==============
 
     def aggregate(self):
        print("\n Aggregate Functions")
        print("Sum:", np.sum(self.arr))
        print("Product:", np.prod(self.arr))
        print("Minimum:", np.min(self.arr))
        print("Maximum:", np.max(self.arr))
        
# =========== statistics ==============

     def statistics(self):
        print("\n Statistical Functions ")
        print("Mean:", np.mean(self.arr))
        print("Median:", np.median(self.arr))
        print("Standard Deviation:", np.std(self.arr))
        print("Variance:", np.var(self.arr))
     def operations(self):
        self.input_array()
        self.aggregate()
        self.statistics()

ag=compute_aggregates_statics()
ca=create_array()
mo=mathematical_operations()
cs=combine_split_arrays()
sa=search_sort_filter_arrays()

# =============== MAIN MENU ===================

while True:
    print("\nMain Menu:")
    print("1. Create Array (with Indexing/Slicing)")
    print("2. Mathematical Operations")
    print("3. comnine and split arrays")
    print("4.Search / Sort / Filter")
    print("5. Aggregate & Statistics")
    print("6. Exit")

    choice = int(input("Enter choice: "))
    match choice:
            case 1:
                print("\n--- Create Array Menu ---")
                print("1. Create 1D Array")
                print("2. Create 2D Array")
                print("3. Create 3D Array")
                sub = int(input("Enter your choice: "))
                if sub == 1:
                    ca.create_1D()
                elif sub == 2:
                    ca.create_2d_array()
                elif sub == 3:
                    ca.create_3d_array()
                else:
                    print("Invalid choice!")
            case 2: mo.operations()
            case 3:
             print("\n--- Combine / Split Menu ---")
             print("1. Combine Arrays")
             print("2. Split Array")
             sub = int(input("Enter your choice: "))
             if sub == 1: cs.combine_arrays()
             elif sub == 2: cs.split_array()
             else: 
                 print("Invalid choice!")
            case 4:
             sa.operations()
            case 5:
             ag.operations()
            case 6:
             print("Exiting program...")
             break
            case _:
                print("Invalid choice!")
                continue
             