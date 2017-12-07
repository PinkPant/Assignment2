# Setup instructions for 201701COMP351AB1s26 / assignment1

heat-deploy.yaml is adequate has it has default values already contained
in heat-deploy.env.yaml

## Prepare deploy key

The ecdsa key is preferable to the RSA key because it is shorter.
This key is specific to one repository/project.

```bash
ssh-keygen -t ecdsa -b 256 -f id_ecdsa 
```

Modify the resulting private key `id_ecdsa` so line breaks get replaced
with percent `%` symbols.

On Linux, you can script this step as follows:
```bash
tr '\n' '%' < id_ecdsa > onelinekey.txt
```

Then insert the one-line key into the `heat-deploy.env.yaml` file in the
appropriate parameter: *deploy_private_key*

The corresponding *public key* stored in `id_ecdsa.pub` should be added as a
deploy key to the *private* git repository containing the source code.

## Set up authorized_keys

Modify the *public_keys_url* parameter to point to your public keys (works on
github accounts too), such as https://cisgitlab.ufv.ca/Rajani_Saini.keys

## Create Stack

Upon logging into CIS OpenStack, click on Orchestration and then Stacks.

Click Launch Stack. Under Template Source, select Direct Input.

In the Template Data box, copy and paste the raw contents at the following URL:
https://cisgitlab.ufv.ca/201701COMP351AB1s26/assignment1/raw/master/orchestration/heat-deploy.yaml

Click Next.

Enter a Stack Name and a password in the password field. Click Launch.

Under Compute, click on Instances. Look for an instance with the same name as the
stack that was created.

Connect to the instance using SSH and/or select Console under Actions.
