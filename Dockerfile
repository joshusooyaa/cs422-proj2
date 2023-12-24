FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8080
MAINTAINER Josh Sawyer "thejoshsawyer@gmail.com"
RUN apt-get update -y
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py import_courses forecast/recommendcourses.xlsx
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "cs_degree_planner.wsgi:application"]
