# Usage guidelines

This is the tool for deploying and dropping entire Log Collector platform or each component separately.

There're other useful functions as well such as:
  - stopping
  - starting
  - configuring

entire Log Collector platform or each component individually.

List of all available tags are in vars/tags.yml file.


## 1) Installing and configuring
- all
  
    ansible-playbook site.yml

- one
  
      ansible-playbook site.yml --tags 'elasticsearch'
    
*another tags:*
   - kafka
   - zookeeper
   - logstash
   - kibana
   - filebeat,beat
   - metricbeat,beat


## 2) Deleting

- all

    ansible-playbook site.yml --tags 'remove'

- one
 
    ansible-playbook site.yml --tags 'elasticsearch_remove'

*another tags:*
   - kafka_remove
   - zookeeper_remove
   - logstash_remove
   - kibana_remove
   - filebeat,beat_remove
   - metricbeat,beat_remove

## 3) Stopping
  
- all
  
    ansible-playbook site.yml --tags 'stop'

- one
  
    ansible-playbook site.yml --tags 'elasticsearch_stop'

*another tags:*
   - kafka_stop
   - zookeeper_stop
   - logstash_stop
   - kibana_stop
   - filebeat,beat_stop
   - metricbeat,beat_stop

## 4) Starting

- all
  
    ansible-playbook site.yml --tags 'start'

- one
    
    ansible-playbook site.yml --tags 'elasticsearch_start'

*another tags:*
   - kafka_start
   - zookeeper_start
   - logstash_start
   - filebeat,beat_start
   - kibana_start
   - metricbeat,beat_start

## 5) Restarting

- all:
    
      ansible-playbook site.yml --tags 'stop,start'
   
- one
    
      ansible-playbook site.yml --tags 'elasticsearch_stop,elasticsearch_start'

#### stop and start tags one after another. Exception:
Beats:
       
        filebeat,beat_stop,beat_start
        
        metricbeat,beat_stop,beat_start


## 6) Configuring
  
- all
    
    ansible-playbook site.yml --tags 'config'

- one
    
    ansible-playbook site.yml --tags 'elasticsearch_config'
    
*another tags*:
   - kafka_config
   - zookeeper_config
   - logstash_config
   - kibana_config
   - filebeat,beat_config
   - metricbeat,beat_config



## MISC
There's also an additional tag for kafka for topic management (_create, remove, alter_):
  - kafka_topic
   
## !!Caution!!

Beats share the same role and it's crucial to spesify beat type in tags. If you need to perform the same action for several type of beat there's no need to repeat action itself but only beat type. For example, to configure both filebeat and metricbeat run:

    ansible-playbook site.yml --tags 'filebeat,metricbeat,beat_config'
    
It activates two roles and executes necessary tasks.
