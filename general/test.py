import list_utils as lu
a = [5,3,1,4,10]

indexes = lu.get_top_k_indexes_of_list(target_list=a, k=2, is_max=True)

print lu.get_elements_from_list(a, indexes)
