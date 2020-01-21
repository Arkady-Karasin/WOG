FROM python:3
COPY requirements.txt /wog/requirements.txt
WORKDIR /wog
RUN pip install Flask
RUN pip install selenium
ADD . /wog
CMD ["python", "./MainScores.py"]