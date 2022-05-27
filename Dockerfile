FROM carbanx/jmeter

COPY testingScript.py /

COPY TrainingNormal.jmx /
COPY TrainingLoad.jmx /
COPY TrainingPeaks.jmx /
COPY TrainingStress.jmx /
COPY TrainingWordLoad.jmx /

CMD ["ls", "/"]