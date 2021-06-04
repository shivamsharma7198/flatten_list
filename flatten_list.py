input_list =[1, [2, 3, [4, 5, 6], [ 7, [ 8, 9, [10, 11], 12] ]]]
output_list = []
for i in input_list:
   if type(i) is list:
        for j in i:
             if type(j) is list:
                 for k in j:
                      if type(k) is list:
                         for k_val in k:
                             print(type(k_val))
                             if type(k_val) is list:
                                 for l_val in k_val:
                                      output_list.append(l_val)
                             else:
                                  output_list.append(k_val)

             else:
                  output_list.append(j)
   else:
         output_list.append(i)

print(output_list)