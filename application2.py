import streamlit as st
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

def main():
    st.title('Diamond Prediction App')

    st.write('Fill in the following details:')
    
    carat = st.text_input('Carat:', value='0.5')
    depth = st.text_input('Depth:', value='60')
    table = st.text_input('Table:', value='55')
    x = st.text_input('x:', value='5')
    y = st.text_input('y:', value='5')
    z = st.text_input('z:', value='5')
    
    cut = st.selectbox('Cut:', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    color = st.selectbox('Color:', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
    clarity = st.selectbox('Clarity:', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

    if st.button('Predict'):
        data = CustomData(
            carat=float(carat),
            depth=float(depth),
            table=float(table),
            x=float(x),
            y=float(y),
            z=float(z),
            cut=cut,
            color=color,
            clarity=clarity
        )
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)
        results = round(pred[0], 2)

        st.write('### Prediction Result:')
        st.write(f'Predicted Diamond Price: {results}')

if __name__ == "__main__":
    main()
