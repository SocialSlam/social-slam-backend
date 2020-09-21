#!/bin/bash
ret=`yes | python manage.py makemigrations`;
if [ "$ret" != "No changes detected" ]; then
   python manage.py migrate
else
  echo "Nothing to migrate"
fi
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='social_slam_admin') or User.objects.create_superuser('social_slam_admin', 'admin@social_slam.com', 'social_slamming_2020')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000 --setting=settings.settings_stage;