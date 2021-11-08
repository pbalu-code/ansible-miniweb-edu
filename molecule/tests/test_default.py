def test_apache2_running(host):
    if host.system_info.distribution in ("redhat", "centos"):
        name = "httpd"
    else:
        name = "apache2"
    service = host.service(name)
    assert service.is_running
    assert service.is_enabled

def test_apache2_http(host):
    miniweb = host.socket('tcp://0.0.0.0:80')
    assert miniweb.is_listening

def test_miniweb_on_http(host):
    output = host.check_output('wget -qO- 0.0.0.0:80')
    assert 'The PHP is working well' in output

