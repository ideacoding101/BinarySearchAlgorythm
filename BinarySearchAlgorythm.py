def BinarySearchAlgorithm(List, Left, Right, Target):
    while (Left <= Right):
        Center = int(Left +(Right - Left) / 2)
        if (Target == List[Center]):
            return ("The number is {}".format(List[Center]))
        if (List[Center] > Target):
                Right = Center - 1
        else:
            Left = Center + 1 
    return ("Unable to find the selected number")

List = [4, 12, 25, 39, 40, 47]
Target = 47
Length = len(List)
Result = BinarySearchAlgorithm(List, 0, Length - 1, Target)
print(Result)
