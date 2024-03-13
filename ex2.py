def get_cats_info(path:str) -> dict:
    """
    Fn returns cats info from raw data

    Args:
        path (str): path to file    

    Returns:
        dict: info about cats (id, name, age)
    """

    try:
        with open(path) as f:
            lines = f.readlines()
            serialized_data = [line.strip().split(',') for line in lines]
            result = [{'id': cat[0], 'name':cat[1], 'age': cat[2] } for cat in serialized_data]
            print(result)
    except FileNotFoundError:
        print(f'Sorry, but path {path} is not exists!')
   
      

get_cats_info('cats.txt')