import streamlit as st
import pandas as pd


def main():
    st.title("Базы данных научно-технической документации по производству животноводческой и растениеводческой продукции ")

    # Navigation
    pages = ["Главная", "НПА", "Рекомендации|Животноводство", "Рекомендации|Растениеводство", "Словари", "Поиск"]

    # Create a horizontal sidebar with buttons for navigation
    selected_page = st.sidebar.radio("Навигация по сайту", pages)


    if selected_page:
        navigate_to(selected_page)


def navigate_to(page):
    st.header(f" {page}")

    # Display specific content based on the selected page
    if page == "Главная":
        home_page()
    elif page == "НПА":
        page_1()
    elif page == "Рекомендации|Животноводство":
        page_2()
    elif page == "Рекомендации|Растениеводство":
        page_3()
    elif page == "Словари":
        page_4()
    elif page == "Поиск":
        page_5()


def home_page():
    st.header("OpenAgro")

    st.image("homepage.jpg", caption="", use_column_width=True)
    markdown_table = """
        | Openagro            | предоставляет                                       |
        |-----------------------|----------------------------------------------------|
        | 1.         | нормативно-техническую документацию по агропромышленному комплексу;            |
        | 2.         | справочную информацию по АПК;                        |
        | 3.         | методические пособия для ведения сельского хозяйства и АПК в целом.       |
        """
    st.markdown(markdown_table)


def page_1():
    df = pd.read_excel('Таблица_НПА_28092023.xlsx')
    st.markdown("<style>body { font-family: 'Arial', sans-serif; }</style>", unsafe_allow_html=True)
    st.dataframe(df, height=700)

def page_2():
    df = pd.read_excel('Животноводство.xlsx')
    st.dataframe(df, height=250, width=700)


def page_3():
    df = pd.read_excel('Растениеводство.xlsx')
    st.dataframe(df, height=240)


def page_4():
    st.write("Пример простого словаря. Типы почв.")
    df = pd.read_excel('простой словарь типы почв.xlsx')
    st.dataframe(df)
    st.write("Конструктор для создания простых словарей.")
    df2 = pd.read_excel('конструктор_словарь_простой_структура.xlsx')
    st.dataframe(df2)
    st.write("Конструктор для создания древовидных словарей.")
    df3 = pd.read_excel('конструктор_древовидный.xlsx')
    st.write(df3)

def page_5():
    st.write("Поиск по ключевой фразе/ каталогизатору.")
    df = pd.read_excel('демо версия текстового поиска файлов данных.xlsx')
    # Search functionality
    search_term = st.text_input("Введите данные для поиска:")

    if search_term:
        filtered_df = df[df['Текстовая версия'].str.contains(search_term, case=False,na=False)]
        st.write(f"Ответ '{search_term}':")
        st.dataframe(filtered_df, height=150)

if __name__ == "__main__":
    main()
