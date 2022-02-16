from .models import TopCustomer


def top_customers(customers):
    select_list = sorted(
        customers.items(), key=lambda x: x[1]['spent_money'], reverse=True
    )[:5]
    obj_list = []
    for i in range(len(select_list)):
        for j in range(i + 1, len(select_list)):
            inters = select_list[i][1]['gems'] & select_list[j][1]['gems']
            select_list[i][1]['select'] |= inters
            select_list[j][1]['select'] |= inters
        obj_list.append(
            TopCustomer(
                username=select_list[i][0],
                spent_money=select_list[i][1]['spent_money'],
                gems=list(select_list[i][1]['select'])
            )
        )
    return obj_list
