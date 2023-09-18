
def intelligent_design_sort(my_list):
    """Sort a list of numbers using the intelligent design sort algorithm."""
    print(my_list)
    return "Since there is 1/n! chance that this list is in this particular order, it is sorted. There is such a small likelihood of this that it's clearly absurd to say that this happened by chance, so it must have been consciously put in that order by an intelligent Sorter. Therefore it's safe to assume that it's already optimally Sorted in some way that transcends our naïve mortal understanding of ascending order. Any attempt to change that order to conform to our own preconceptions would actually make it less sorted"

def main():
    """Test the intelligent_design_sort function."""
    print(intelligent_design_sort([1, 2, 3, 4, 5]))
    print(intelligent_design_sort([5, 4, 3, 2, 1]))

if __name__ == '__main__':
    main()