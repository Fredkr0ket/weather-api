class WeatherItem(Base):
  __tablename__ = "weatherdata"

  id = Column(Integer, primary_key=True, index=True)
  location = Column(string, default=None)
  temperature = Column(Integer, default=False)
  humidity = Column(Integer, default=False)
  weather_date = Column(datatime.datatime, default=current_timestamp)

