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

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_detail = error_detail

def main():
    st.title('Diamond Prediction App')

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
            st.error(f"CustomException details: {e.error_detail}")
        
        except Exception as e:
            st.error("An unexpected error occurred.")
            st.error(f"Error details: {e}")

if __name__ == "__main__":
    main()
