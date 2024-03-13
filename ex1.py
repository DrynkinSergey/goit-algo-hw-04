def get_salaries_info(path:str)->tuple:
    """Take the salaries from raw data file and return info

    Args:
        path (string): Path to file in format (.txt)

    Returns:
        tuple : total sum, average sum 
    """

    try:
        with open(path) as f:
            lines  = f.readlines()
            if not(len(lines)):
               return (0, 0)
            
            serialized_data = [int(line.strip().split(',')[1]) for line in lines]
            sum_salary = sum(serialized_data) 
            avg = sum_salary / len(serialized_data)
        return sum_salary , avg 
    except FileNotFoundError:
        print(f'Sorry, but path {path} is not exists!')
   
  

print(get_salaries_info('example.txt'))