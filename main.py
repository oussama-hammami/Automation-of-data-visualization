import pandas as pd 
import matplotlib.pyplot as plt 
import streamlit as st 

file = st.file_uploader("Insert the CSV file", type=["csv"])
if file == None:
    data = pd.DataFrame(list([]))
else:
    data = pd.read_csv(file)
dict = {}

st.write(data.head(5))

columlist = data.columns

st.sidebar.markdown("## Select specification")

for i in data.columns:
	def verif(i):
		col = set(data[i].tolist())
		return len(col) < len(data[i]) / 10 or len(col) < 20
	if verif(i):
		dict[i] = st.sidebar.multiselect(i,
                                    list(set(data[i].tolist())))

	else:
		dict[i] = st.sidebar.text_input(
        f"condition on {i}",
        label_visibility="visible",
        disabled=False,
        placeholder=f"max = {max(data[i])} and min = {min(data[i])}",
    )

condition = ''
for i in dict.keys():
	if type(dict[i ]) == str and dict[i] != '':
		condition = condition + f"{i} {dict[i]} and "
	if type(dict[i]) != str and dict[i] != []:
		condition  = condition + f"{i} in {dict[i]} and "

st.sidebar.markdown("## Set axis")

X_axis = st.sidebar.selectbox("X axis", data.columns.tolist())
Y_axis = st.sidebar.selectbox("Y axis", data.columns.tolist())


try:
	if condition != '':
		data1 = data.query(condition[:-4])
	else:
		data1=data
	x1 = data1[X_axis]
	y1 = data1[Y_axis]

	fig, ax = plt.subplots()
	ax.scatter(x1,y1, s = 1)
	ax.set_title(f"{Y_axis} = f({X_axis})")
	ax.set(xlabel=X_axis, ylabel=Y_axis)

	st.pyplot(fig)

except:
	st.write("Information are not valid")

