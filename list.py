def list(name1,name2,name3,name4,name5):
    from rich.console import Console
    from rich.table import Table
    from rich import box

    table = Table(title='LIST', box=box.ROUNDED, show_lines=True,
                header_style='bold magenta', row_styles=['', 'dim'])

    table.add_column('NAME', style='white', no_wrap=True)
    table.add_column('NUMBER', justify='center')
  
    table.add_row(name1, "1")   
    table.add_row(name2, "2")
    table.add_row(name3, "3")
    table.add_row(name4, "4")
    table.add_row(name5, "5")

    table.add_section()                                  
    Console().print(table)

def main():
    name1 = input("enter first name: ")
    name2 = input("enter second name: ")
    name3 = input("enter the third name: ")
    name4 = input("enter the forth name: ")
    name5 = input("enter the fifth name: ")
    list(name1,name2,name3,name4,name5)

main()


