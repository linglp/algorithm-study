peg1=[1, 2, 3]
peg2=[]
peg3=[]


# define a base case
# the base case should be as simple as moving disk 1 to destination 
# if the algorithm is correct, there's always no need to worry about checking if you are always moving the smallest disk
def move_disk(location1, location2, piece):
    # Move pieces from location 1 to location 2
    location1.remove(piece)

    location2.insert(0, piece)


    return location1, location2


def hanoi2(peg1, peg2, peg3, num_disks, source, storage, destination):

    if num_disks > 0:
        # move all the disks (1-9) to storage, and then move disk 10 to destination
        hanoi2(peg1, peg2, peg3, num_disks-1, source, destination, storage)
        move_disk(source, destination, num_disks)
        # move all the disks (1-9) from storage to destination
        hanoi2(peg1, peg2, peg3, num_disks-1, storage, source, destination)
    return peg1, peg2, peg3

peg1, peg2, peg3 = hanoi2(peg1, peg2, peg3, num_disks=len(peg1), source=peg1, storage=peg2, destination=peg3)
