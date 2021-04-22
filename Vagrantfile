Vagrant.configure("2") do |config|
  # config.vm.box = "centos/7"
  config.vm.box = "generic/debian9"

  config.vm.box_check_update = false

  config.vm.network "forwarded_port", guest: 80, host: 8089
  # config.vm.network "private_network", type: "dhcp"
  # config.vm.network :private_network, ip: "192.168.68.8"

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update 
    apt install wget
    wget downloads.sourceforge.net/openemr/openemr-php7_5.0.1-2_all.deb 
    dpkg -i openemr-php7_5.0.1-2_all.deb
    apt-get -f install
    apt-get install -y git
    git clone https://github.com/openemr/demo-data-generator.git
  SHELL
end
