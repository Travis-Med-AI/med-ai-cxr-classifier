FROM ai-model:latest as model
FROM tensorflow/tensorflow:2.0.0-gpu-py3

# DONT EDIT THIS SECTION
# add current directory to container
COPY --from=model /opt/runner /opt
WORKDIR /opt
ADD . /opt/
RUN pip install redis
CMD python runner.py

# Install dependencies
RUN pip install pydicom scikit-image
