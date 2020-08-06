FROM tclarke104/ai-model-base:0.1 as model
# FROM tensorflow/tensorflow:2.0.0-py3
FROM tensorflow/tensorflow:2.0.0-gpu-py3

# Install dependencies
RUN pip install pydicom scikit-image medaimodels

# DONT EDIT THIS SECTION
# add current directory to container
RUN pip install redis
COPY --from=model /opt/runner /opt
WORKDIR /opt
ADD . /opt/
CMD python runner.py

# CMD python main.py
