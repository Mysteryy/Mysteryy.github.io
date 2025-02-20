from regex import match


class DataSet:
    def __init__(self):
        self.data_a = [('USA', 'DC'), ('Russia', 'Moscow'), ('a', 'b'), ('country', 'capital')]
        self.data_b = [('USA', 'DC'), ('Russia', 'Moscow'), ('a', 'b'), ('country', 'capital')]


class Implementation:
    def update_list(self, input_list, country, new_capital):
        for i in range(len(input_list)):
            co, ca = input_list[i]
            if co == country:
                input_list[i] = (country, new_capital)
                break

        return input_list

    def update_countries_ending_with(self, input_list, letter, new_capital):
        for i in range(len(input_list)):
            co, ca = input_list[i]
            if str(co).endswith(letter):
                input_list[i] = (co, new_capital)

        return input_list

    def update_countries_countaining(self, input_list, sub_str, new_capital):
        for i in range(len(input_list)):
            co, ca = input_list[i]
            if sub_str in co:
                input_list[i] = (co, new_capital)

        return input_list

    def update_countries_with_case(self, input_list, new_capital):
        for i in range(len(input_list)):
            co, ca = input_list[i]
            if match('[A-Z].*[a-z]$', co):
                input_list[i] = (co, new_capital)

        return input_list


if __name__ == '__main__':
    data_set = DataSet()
    implementation = Implementation()
    print(implementation.update_countries_with_case(data_set.data_a, 'un', 'new_capital'))
