FROM java:8
ADD server-0.1.15-SNAPSHOT-fat-tests.jar server-0.1.15-SNAPSHOT-fat-tests.jar
ADD dynamic_config.json dynamic_config.json
EXPOSE 5678
CMD java -jar server-0.1.15-SNAPSHOT-fat-tests.jar dynamic_config.json "0 0/5 * * * ? *" --logLevel=WARN
