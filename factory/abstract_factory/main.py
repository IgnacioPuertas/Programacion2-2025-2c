from .store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); chi = ChicagoPizzaStore()
    ny.order_pizza("cheese")
    chi.order_pizza("clam")
    chi.order_pizza("veggie")


if __name__ == "__main__":
    main()