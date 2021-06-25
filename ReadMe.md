<div class="_main--content-container--ILkoI"><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h2 id="starter-code-and-data">Starter Code and Data</h2>
<p>Please find in the Resources tab, in the left sidebar of your classroom here, a zip file with all of the starter files and code referred to here in these directions. You can download those files and run your code locally, or you can use the Project Workspace we provide.</p>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h2 id="project-directions">Project Directions</h2>
<p>The Chicago Transit Authority (CTA) has asked us to develop a dashboard displaying system status for its commuters. We have decided to use Kafka and ecosystem tools like REST Proxy and Kafka Connect to accomplish this task.</p>
<p>Our architecture will look like so:</p>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div><div role="button" tabindex="0" aria-label="Show Image Fullscreen" class="image-atom--image-atom--1XDdu"><div class="image-atom-content--CDPca"><div class="image-and-annotations-container--1U01s"><img class="image--26lOQ" src="https://video.udacity-data.com/topher/2019/July/5d320154_screen-shot-2019-07-19-at-10.43.38-am/screen-shot-2019-07-19-at-10.43.38-am.png" alt="" width="1758px"></div></div></div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h4 id="step-1-create-kafka-producers">Step 1: Create Kafka Producers</h4>
<p>The first step in our plan is to configure the train stations to emit some of the events that we need. The CTA has placed a sensor on each side of every train station that can be programmed to take an action whenever a train arrives at the station.</p>
<p>To accomplish this, you must complete the following tasks:</p>
<ol>
<li><p>Complete the code in <code>producers/models/producer.py</code>.</p>
</li>
<li><p>Define a value schema for the arrival event in <code>producers/models/schemas/arrival_value.json</code> with the following attributes:</p>
<ul>
<li>station_id</li>
<li>train_id</li>
<li>direction</li>
<li>line</li>
<li>train_status</li>
<li>prev_station_id</li>
<li>prev_direction</li>
</ul>
</li>
<li>Complete the code in <code>producers/models/station.py</code> so that:<ul>
<li>A topic is created for each station in Kafka to track the arrival events</li>
<li>The station emits an arrival event to Kafka whenever the <code>Station.run()</code> function is called.</li>
<li>Ensure that events emitted to Kafka are paired with the Avro key and value schemas</li>
</ul>
</li>
<li>Define a value schema for the turnstile event in <code>producers/models/schemas/turnstile_value.json</code> with the following attributes<ul>
<li>station_id</li>
<li>station_name</li>
<li>line</li>
</ul>
</li>
<li>Complete the code in <code>producers/models/turnstile.py</code> so that:<ul>
<li>A topic is created for each turnstile for each station in Kafka to track the turnstile events</li>
<li>The station emits a turnstile event to Kafka whenever the <code>Turnstile.run()</code> function is called.</li>
<li>Events emitted to Kafka are paired with the Avro key and value schemas</li>
</ul>
</li>
</ol>
<blockquote>
<p><strong>Note</strong> </p>
<ul>
<li>Make sure that you "Save" files after editing. The workspace does not support "AutoSave" functionality.</li>
<li>You would not be able to edit JSON files directly in the workspace. You can edit them locally and then upload them to the workspace.</li>
</ul>
</blockquote>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h4 id="step-2-configure-kafka-rest-proxy-producer">Step 2: Configure Kafka REST Proxy Producer</h4>
<p>Our partners at the CTA have asked that we also send weather readings into Kafka from their weather hardware. Unfortunately, this hardware is old and we cannot use the Python Client Library due to hardware restrictions. Instead, we are going to use HTTP REST to send the data to Kafka from the hardware using Kafka's REST Proxy.</p>
<p>To accomplish this, you must complete the following tasks:</p>
<ol>
<li>Define a value schema for the weather event in <code>producers/models/schemas/weather_value.json</code> with the following attributes:<ul>
<li>temperature</li>
<li>status</li>
</ul>
</li>
<li>Complete the code in <code>producers/models/weather.py</code> so that:<ul>
<li>A topic is created for weather events</li>
<li>The weather model emits weather event to Kafka REST Proxy whenever the Weather.run() function is called.<ul>
<li>NOTE: When sending HTTP requests to Kafka REST Proxy, be careful to include the correct Content-Type. Pay close attention to the <a target="_blank" href="https://docs.confluent.io/current/kafka-rest/api.html#post--topics-(string-topic_name">examples in the documentation</a> for more information.</li>
</ul>
</li>
<li>Events emitted to REST Proxy are paired with the Avro key and value schemas</li>
</ul>
</li>
</ol>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h4 id="step-3-configure-kafka-connect">Step 3: Configure Kafka Connect</h4>
<p>Finally, we need to extract station information from our PostgreSQL database into Kafka. We've decided to use the <a target="_blank" href="https://docs.confluent.io/current/connect/kafka-connect-jdbc/source-connector/index.html">Kafka JDBC Source Connector</a>.</p>
<p>To accomplish this, you must complete the following tasks:</p>
<ol>
<li>Complete the code and configuration in producers/connectors.py<ul>
<li>Please refer to the <a target="_blank" href="https://docs.confluent.io/current/connect/kafka-connect-jdbc/source-connector/source_config_options.html">Kafka Connect JDBC Source Connector Configuration Options</a> for documentation on the options you must complete.</li>
<li>You can run this file directly to test your connector, rather than running the entire simulation.</li>
<li>Make sure to use the Kafka Connect API, kafka-console-consumer, and kafka-topics CLI tool to check the status and output of the Connector</li>
<li>To delete a misconfigured connector: CURL -X DELETE localhost:8083/connectors/stations</li>
</ul>
</li>
</ol>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h4 id="step-4-configure-the-faust-stream-processor">Step 4: Configure the Faust Stream Processor</h4>
<p>We will leverage Faust Stream Processing to transform the raw Stations table that we ingested from Kafka Connect. The raw format from the database has more data than we need, and the line color information is not conveniently configured. To remediate this, we're going to ingest data from our Kafka Connect topic, and transform the data.</p>
<p>To accomplish this, you must complete the following tasks:</p>
<ul>
<li>Complete the code and configuration in <code>consumers/faust_stream.py</code></li>
</ul>
<p><strong>Watch Out!</strong>
You must run this Faust processing application with the following command:</p>
<p><code>faust -A faust_stream worker -l info</code></p>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h4 id="step-5-configure-the-ksql-table">Step 5: Configure the KSQL Table</h4>
<p>Next, we will use KSQL to aggregate turnstile data for each of our stations. Recall that when we produced turnstile data, we simply emitted an event, not a count. What would make this data more useful would be to summarize it by station so that downstream applications always have an up-to-date count.</p>
<p>To accomplish this, you must complete the following tasks:</p>
<ul>
<li>Complete the queries in <code>consumers/ksql.py</code>.</li>
</ul>
<p><strong>Tips</strong></p>
<ul>
<li>The KSQL CLI is the best place to build your queries. Try <code>ksql</code> in your workspace to enter the CLI.</li>
<li>You can run this file on its own simply by running <code>python ksql.py</code>.</li>
<li>Made a mistake in table creation? <code>DROP TABLE &lt;your_table&gt;</code>. If the CLI asks you to terminate a running query, you can <code>TERMINATE &lt;query_name&gt;</code>.</li>
</ul>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h4 id="step-6-create-kafka-consumers">Step 6: Create Kafka Consumers</h4>
<p>With all of the data in Kafka, our final task is to consume the data in the web server that is going to serve the transit status pages to our commuters.</p>
<p>To accomplish this, you must complete the following tasks:</p>
<ol>
<li>Complete the code in <code>consumers/consumer.py</code></li>
<li>Complete the code in <code>consumers/models/line.py</code></li>
<li>Complete the code in <code>consumers/models/weather.py</code></li>
<li>Complete the code in <code>consumers/models/station.py</code></li>
</ol>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h3 id="other-resources-and-documentation">Other Resources and Documentation</h3>
<p>In addition to the course content you have already reviewed, you may find the following examples and documentation helpful in completing this project:</p>
<ul>
<li><p><a target="_blank" href="https://docs.confluent.io/current/clients/confluent-kafka-python/#">Confluent Python Client Documentation</a></p>
</li>
<li><p><a target="_blank" href="https://github.com/confluentinc/confluent-kafka-python#usage">Confluent Python Client Usage and Examples</a></p>
</li>
<li><p><a target="_blank" href="https://docs.confluent.io/current/kafka-rest/api.html#post--topics-(string-topic_name">REST Proxy API Reference</a></p>
</li>
<li><p><a target="_blank" href="https://docs.confluent.io/current/connect/kafka-connect-jdbc/source-connector/source_config_options.html">Kafka Connect JDBC Source Connector Configuration Options</a></p>
</li>
</ul>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h3 id="directory-layout">Directory Layout</h3>
<p>The project consists of two main directories, <code>producers</code> and <code>consumers</code>.</p>
<p>The following directory layout indicates with a * the files that the student is responsible for modifying. Instructions for what is required are present as comments in each file.</p>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div><div role="button" tabindex="0" aria-label="Show Image Fullscreen" class="image-atom--image-atom--1XDdu"><div class="image-atom-content--CDPca"><div class="image-and-annotations-container--1U01s"><img class="image--26lOQ" src="https://video.udacity-data.com/topher/2019/July/5d3518ca_screen-shot-2019-07-21-at-7.00.34-pm/screen-shot-2019-07-21-at-7.00.34-pm.png" alt="" width="1776px"></div></div></div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h2 id="running-and-testing">Running and Testing</h2>
<h3 id="running-in-the-classroom-project-workspace-recommended-">Running in the Classroom Project Workspace (recommended)</h3>
<p>The Project Workspace environment is already preconfigured with all of the services you need to complete your project. No additional configuration is required.</p>
<p>The following services are available in the classroom workspace environment:</p>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div><div role="button" tabindex="0" aria-label="Show Image Fullscreen" class="image-atom--image-atom--1XDdu"><div class="image-atom-content--CDPca"><div class="image-and-annotations-container--1U01s"><img class="image--26lOQ" src="https://video.udacity-data.com/topher/2019/September/5d71588a_screen-shot-2019-09-05-at-11.47.37-am/screen-shot-2019-09-05-at-11.47.37-am.png" alt="" width="1588px"></div></div></div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h3 id="running-on-your-computer">Running on Your Computer</h3>
<p><strong>NOTE: You must allocate <em>at least</em> 4gb RAM to your Docker-Compose environment to run locally.</strong></p>
<p>To run the simulation, you must first start up the Kafka ecosystem on your machine utilizing Docker-Compose.</p>
<p><code>%&gt; docker-compose up</code></p>
<p>Docker-Compose will take 3-5 minutes to start, depending on your hardware. Please be patient and wait for the Docker-Compose logs to slow down or stop before beginning the simulation.</p>
<p>Once Docker-Compose is ready, the following services will be available on your local machine:</p>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div><div role="button" tabindex="0" aria-label="Show Image Fullscreen" class="image-atom--image-atom--1XDdu"><div class="image-atom-content--CDPca"><div class="image-and-annotations-container--1U01s"><img class="image--26lOQ" src="https://video.udacity-data.com/topher/2019/September/5d715921_screen-shot-2019-09-05-at-11.50.46-am/screen-shot-2019-09-05-at-11.50.46-am.png" alt="" width="1586px"></div></div></div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><p>Note that to access these services from your own machine, you will always use the <code>Host URL</code> column.</p>
<p>When configuring services that run within Docker-Compose, like Kafka Connect, <strong>you must use the <code>Docker URL</code></strong>. When you configure the JDBC Source Kafka Connector, for example, you will want to use the value from the <code>Docker URL</code> column.</p>
<h3 id="running-the-simulation">Running the Simulation</h3>
<p>There are two pieces to the simulation, the <code>producer</code> and <code>consumer</code>. As you develop each piece of the code, it is recommended that you only run one piece of the project at a time.</p>
<p>However, when you are ready to verify the end-to-end system prior to submission, it is critical that you open a terminal window for each piece and run them at the same time. <strong>If you do not run both the <code>producer</code> and <code>consumer</code> at the same time you will not be able to successfully complete the project.</strong></p>
<p><strong>To run the <code>producer</code>:</strong></p>
<p>If using Project Workspace:</p>
<ol>
<li><code>cd producers</code></li>
<li><code>python simulation.py</code></li>
</ol>
<p>If using your computer:</p>
<ol>
<li><code>cd producers</code></li>
<li><code>virtualenv venv</code></li>
<li><code>. venv/bin/activate</code></li>
<li><code>pip install -r requirements.txt</code></li>
<li><code>python simulation.py</code></li>
</ol>
<p>Once the simulation is running, you may hit <code>Ctrl+C</code> at any time to exit.</p>
<p><strong>To run the Faust Stream Processing Application:</strong></p>
<p>If using Project Workspace:</p>
<ol>
<li><code>cd consumers</code></li>
<li><code>faust -A faust_stream worker -l info</code></li>
</ol>
<p>If using your computer:</p>
<ol>
<li><code>cd consumers</code></li>
<li><code>virtualenv venv</code></li>
<li><code>. venv/bin/activate</code></li>
<li><code>pip install -r requirements.txt</code></li>
<li><code>faust -A faust_stream worker -l info</code></li>
</ol>
<p><strong>To run the KSQL Creation Script:</strong></p>
<p>If using Project Workspace:</p>
<ol>
<li><code>cd consumers</code></li>
<li><code>python ksql.py</code></li>
</ol>
<p>If using your computer:</p>
<ol>
<li><code>cd consumers</code></li>
<li><code>virtualenv venv</code></li>
<li><code>. venv/bin/activate</code></li>
<li><code>pip install -r requirements.txt</code></li>
<li><code>python ksql.py</code></li>
</ol>
<p><strong>To run the <code>consumer</code>:</strong>    (<strong>NOTE</strong>: Do not run the consumer until you have reached Step 6!)</p>
<p>If using Project Workspace:</p>
<ol>
<li><code>cd consumers</code></li>
<li><code>python server.py</code></li>
</ol>
<p>If using your computer:</p>
<ol>
<li><code>cd consumers</code></li>
<li><code>virtualenv venv</code></li>
<li><code>. venv/bin/activate</code></li>
<li><code>pip install -r requirements.txt</code></li>
<li><code>python server.py</code></li>
</ol>
<p>Once the server is running, you may hit <code>Ctrl+C</code> at any time to exit.</p>
</div></div><span></span></div></div></div><div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="index-module--markdown--2MdcR ureact-markdown "><h2 id="project-submission">Project Submission</h2>
<p>Please check your work against the project <a target="_blank" href="https://review.udacity.com/#!/rubrics/2660/view">rubric</a> before you submit it. Your reviewer will be using this rubric to assess your project work.</p>
<p>The only thing you need to submit for this project is your code. To do this, you have two options:</p>
<ul>
<li>You may submit a link to your GitHub repo on the project page: "Optimizing Public Transportation."</li>
<li>Or for those of you developing your code in the classroom workspace, you may submit your workspace code directly. </li>
</ul>
</div></div><span></span></div></div></div></div>
