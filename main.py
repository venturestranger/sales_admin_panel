import streamlit as st
from driver import retrieve 
from driver import disable


selected_ad = None


def render_sidebar():
	cheques = retrieve()
	
	global selected_ad

	selected_id = st.sidebar.selectbox('Выберите чек:', list(map(lambda x: f'{x[0]}. {x[1].date}', enumerate(cheques))))

	if selected_id != None:
		selected_ad = cheques[int(selected_id.split('. ')[0])]


def render_page():
	global selected_ad

	if selected_ad != None:
		st.caption('Имя:')
		st.info(f'{selected_ad.name}')
		st.caption('Телефон:')
		st.info(f'{selected_ad.contact}')
		st.caption('Описание:')
		st.info(f'{selected_ad.content}')
		st.caption('Дата:')
		st.info(f'{selected_ad.date}')
		st.caption('Цена:')
		st.info(f'{selected_ad.cost} тг.')

		confirm = st.checkbox('Подтвердить действие')
		close = st.button('Закрыть чек')

		if close and confirm: 
			disable(selected_ad.id)
			st.rerun()
		elif close and not confirm:
			st.error('Вы не подтвердили действие')
	else:
		st.write('Нет доступных чеков')


render_sidebar()
render_page()
