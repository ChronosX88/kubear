gopher://{{data['ip']}}/
Dirs:
{% for node in data['files'] -%}
{% if node['type'] == '1' -%}
 + {{node['path']}}
{% endif -%}
{% endfor -%}
Other nodes:
{% for node in data['files'] -%}
{% if node['type'] != '1' and node['type'] != 'i' -%}
 + {{node['path']}}
     {{node['name']}}
{% endif -%}
{% endfor -%}
Geo: {{data['geo']['country']}}/{{data['geo']['city']}}