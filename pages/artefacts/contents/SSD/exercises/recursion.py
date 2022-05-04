class Solution:

  def tower_of_hanoi(self, n, source, destination, auxiliary):
    '''Recursive function for solving the tower of hanoi problem'''

    # Base case for the recursion function
    if n == 1:
      print(f'Move disk 1 from source {source} to destination {destination}')
      return
    
    # Move from source to auxiliary
    self.tower_of_hanoi(n - 1, source, auxiliary, destination)

    print(f'Move disk {n} from source {source} to destination {destination}')

    # Move from auxiliary to destination
    self.tower_of_hanoi(n-1, auxiliary, destination, source)
  
if __name__ == '__main__':
  n = 4
  Solution().tower_of_hanoi(n, 'A', 'B', 'C')
