def groupingDishes(dishes):
    ingredients = {}
    for dish in dishes:
        for i in range(1, len(dish)):
            if dish[i] in ingredients:
                ingredients[dish[i]].append(dish[0])
            else:
                ingredients[dish[i]] = [dish[0]]
    
    result = []
    for key, value in ingredients.items():
        if len(value) > 1:
            value.sort()
            value.insert(0, key)
            result.append(value)
    
    return sorted(result, key=sort_dish)
    
def sort_dish(item):
    return item[0]

print(groupingDishes([["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
                      ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
                      ["Quesadilla", "Chicken", "Cheese", "Sauce"],
                      ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]))

print(groupingDishes([["Pasta", "Tomato Sauce", "Onions", "Garlic"],
                      ["Chicken Curry", "Chicken", "Curry Sauce"],
                      ["Fried Rice", "Rice", "Onions", "Nuts"],
                      ["Salad", "Spinach", "Nuts"],
                      ["Sandwich", "Cheese", "Bread"],
                      ["Quesadilla", "Chicken", "Cheese"]]))
