# Limit too many files - More users
exec { "sudo sed -i 's/5/3005/g; s/4/3004/g' /etc/security/limits.conf":
  path => '/bin:/usr/bin:/usr/sbin:/sbin',
}
