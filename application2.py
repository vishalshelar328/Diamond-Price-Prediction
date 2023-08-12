import streamlit as st
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline
from src.exception import CustomException

import pandas as pd

class CustomData:
    def __init__(self,
                 carat=float(0.5),
                 depth=float(60),
                 table=float(55),
                 x=float(5),
                 y=float(5),
                 z=float(5),
                 cut='Fair',
                 color='D',
                 clarity='I1'):
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data(self):
        return {
            'carat': self.carat,
            'depth': self.depth,
            'table': self.table,
            'x': self.x,
            'y': self.y,
            'z': self.z,
            'cut': self.cut,
            'color': self.color,
            'clarity': self.clarity
        }

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
        try:
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
            final_new_data = pd.DataFrame(data.get_data(), index=[0])
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_new_data)
            results = round(pred[0], 2)

            st.write('### Prediction Result:')
            st.write(f'Predicted Diamond Price: {results}')
        
        except CustomException as e:
            st.error("An error occurred while processing the prediction.")
            st.error(f"CustomException details: {e.error_detail}")
        
        except Exception as e:
            st.error("An unexpected error occurred.")
            st.error(f"Error details: {e}")

if __name__ == "__main__":
    main()
