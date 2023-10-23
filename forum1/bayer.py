#import numpy as np
#import matplotlib.pyplot as plt
# import seaborn

def calculate_probabilities(dataset):
    total_count = len(dataset)
    purchase_count = len([x for x in dataset if x["Purchase"] == "Yes"])
    
    day_purchase_prob = {}
    discount_purchase_prob = {}
    delivery_purchase_prob = {}

    for instance in dataset:
        day = instance["Day"]
        discount = instance["Discount"]
        delivery = instance["Free"]
        purchase = instance["Purchase"]

        if day not in day_purchase_prob:
            day_purchase_prob[day] = {"Yes": 0, "No": 0}
        if discount not in discount_purchase_prob:
            discount_purchase_prob[discount] = {"Yes": 0, "No": 0}
        if delivery not in delivery_purchase_prob:
            delivery_purchase_prob[delivery] = {"Yes": 0, "No": 0}

        day_purchase_prob[day][purchase] += 1
        discount_purchase_prob[discount][purchase] += 1
        delivery_purchase_prob[delivery][purchase] += 1

    for day, counts in day_purchase_prob.items():
        day_purchase_prob[day]["Yes"] = (day_purchase_prob[day]["Yes"] + 1) / (purchase_count + 2)
        day_purchase_prob[day]["No"] = 1 - day_purchase_prob[day]["Yes"]

    for discount, counts in discount_purchase_prob.items():
        discount_purchase_prob[discount]["Yes"] = (discount_purchase_prob[discount]["Yes"] + 1) / (purchase_count + 2)
        discount_purchase_prob[discount]["No"] = 1 - discount_purchase_prob[discount]["Yes"]

    for delivery, counts in delivery_purchase_prob.items():
        delivery_purchase_prob[delivery]["Yes"] = (delivery_purchase_prob[delivery]["Yes"] + 1) / (purchase_count + 2)
        delivery_purchase_prob[delivery]["No"] = 1 - delivery_purchase_prob[delivery]["Yes"]

    return day_purchase_prob, discount_purchase_prob, delivery_purchase_prob, purchase_count / total_count

def predict_probability(features, day_prob, discount_prob, delivery_prob, prior_prob):
    day, discount, delivery = features
    probability_purchase = (
        day_prob[day]["Yes"] *
        discount_prob[discount]["Yes"] *
        delivery_prob[delivery]["Yes"] *
        prior_prob
    )

    probability_not_purchase = (
        day_prob[day]["No"] *
        discount_prob[discount]["No"] *
        delivery_prob[delivery]["No"] *
        (1 - prior_prob)
    )

    return probability_purchase, probability_not_purchase
def load_dataset():
    dataset = [
        {"Day": "Weekday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Weekday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Weekday", "Discount": "No", "Free": "No", "Purchase": "No"},
        {"Day": "Holiday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Weekend", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Holiday", "Discount": "No", "Free": "No", "Purchase": "No"},
        {"Day": "Weekend", "Discount": "Yes", "Free": "No", "Purchase": "Yes"},
        {"Day": "Weekday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Weekend", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Holiday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Holiday", "Discount": "No", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Holiday", "Discount": "No", "Free": "No", "Purchase": "No"},
        {"Day": "Weekend", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Holiday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Holiday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Weekday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Holiday", "Discount": "No", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Weekday", "Discount": "Yes", "Free": "No", "Purchase": "Yes"},
        {"Day": "Weekend", "Discount": "No", "Free": "No", "Purchase": "Yes"},
        {"Day": "Weekend", "Discount": "No", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Weekday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Weekend", "Discount": "Yes", "Free": "Yes", "Purchase": "No"},
        {"Day": "Holiday", "Discount": "No", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Weekday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Holiday", "Discount": "No", "Free": "No", "Purchase": "No"},
        {"Day": "Weekday", "Discount": "No", "Free": "Yes", "Purchase": "No"},
        {"Day": "Weekday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Weekday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Holiday", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
        {"Day": "Weekend", "Discount": "Yes", "Free": "Yes", "Purchase": "Yes"},
    ]
    return dataset

###
def main():
    dataset = load_dataset()
    day_prob, discount_prob, delivery_prob, prior_prob = calculate_probabilities(dataset)

    features = ("Weekday", "No", "Yes")
    purchase_prob, not_purchase_prob = predict_probability(features, day_prob, discount_prob, delivery_prob, prior_prob)

    print("Probability of Purchase:", purchase_prob)
    print("Probability of Not Purchase:", not_purchase_prob)
    print(":)")

if __name__ == "__main__":
    main()

    
