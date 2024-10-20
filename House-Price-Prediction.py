{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2b66f0fc-2566-489e-b42a-15307b53bad6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/50\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\aravi\\anaconda3\\Lib\\site-packages\\keras\\src\\layers\\core\\dense.py:87: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.\n",
      "  super().__init__(activity_regularizer=activity_regularizer, **kwargs)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 1ms/step - loss: 55534174208.0000 - mae: 205818.2031 - val_loss: 55904661504.0000 - val_mae: 206249.8281\n",
      "Epoch 2/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 790us/step - loss: 55114059776.0000 - mae: 204714.4688 - val_loss: 52514516992.0000 - val_mae: 198696.2344\n",
      "Epoch 3/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 49488715776.0000 - mae: 192796.9062 - val_loss: 44904669184.0000 - val_mae: 180691.8125\n",
      "Epoch 4/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 933us/step - loss: 42294894592.0000 - mae: 174523.2969 - val_loss: 34341281792.0000 - val_mae: 152706.0312\n",
      "Epoch 5/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 771us/step - loss: 30980843520.0000 - mae: 143660.8125 - val_loss: 23568513024.0000 - val_mae: 119743.9531\n",
      "Epoch 6/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 897us/step - loss: 20580515840.0000 - mae: 109506.2109 - val_loss: 15440638976.0000 - val_mae: 91794.8672\n",
      "Epoch 7/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 877us/step - loss: 13538804736.0000 - mae: 84452.3047 - val_loss: 10968294400.0000 - val_mae: 75502.3203\n",
      "Epoch 8/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 965us/step - loss: 9701090304.0000 - mae: 71193.7891 - val_loss: 8985152512.0000 - val_mae: 68136.3359\n",
      "Epoch 9/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 920us/step - loss: 8383833600.0000 - mae: 66000.7891 - val_loss: 8032279552.0000 - val_mae: 64294.4180\n",
      "Epoch 10/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 720us/step - loss: 7538504192.0000 - mae: 62011.7109 - val_loss: 7416349696.0000 - val_mae: 61563.1562\n",
      "Epoch 11/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 822us/step - loss: 6627287552.0000 - mae: 58508.0352 - val_loss: 6963244544.0000 - val_mae: 59386.2344\n",
      "Epoch 12/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 6300741632.0000 - mae: 56874.9609 - val_loss: 6589273600.0000 - val_mae: 57689.1016\n",
      "Epoch 13/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 744us/step - loss: 6001747456.0000 - mae: 55189.2773 - val_loss: 6284547584.0000 - val_mae: 56168.5039\n",
      "Epoch 14/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 752us/step - loss: 5847884288.0000 - mae: 54835.0391 - val_loss: 6021801472.0000 - val_mae: 54989.0195\n",
      "Epoch 15/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 811us/step - loss: 5755922944.0000 - mae: 53856.6172 - val_loss: 5795509760.0000 - val_mae: 54000.6836\n",
      "Epoch 16/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 929us/step - loss: 5383906304.0000 - mae: 52502.4102 - val_loss: 5604448768.0000 - val_mae: 53184.0625\n",
      "Epoch 17/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 910us/step - loss: 5210260992.0000 - mae: 51581.6641 - val_loss: 5446463488.0000 - val_mae: 52510.4883\n",
      "Epoch 18/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 784us/step - loss: 4973032960.0000 - mae: 50612.8047 - val_loss: 5318516736.0000 - val_mae: 51880.1953\n",
      "Epoch 19/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 870us/step - loss: 4952325632.0000 - mae: 50467.6680 - val_loss: 5209549824.0000 - val_mae: 51516.7773\n",
      "Epoch 20/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 4875968512.0000 - mae: 50188.8594 - val_loss: 5121702912.0000 - val_mae: 51293.7734\n",
      "Epoch 21/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 982us/step - loss: 4852305920.0000 - mae: 50433.9766 - val_loss: 5051583488.0000 - val_mae: 50923.2422\n",
      "Epoch 22/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 774us/step - loss: 4940672512.0000 - mae: 50455.0273 - val_loss: 4996297728.0000 - val_mae: 50597.3672\n",
      "Epoch 23/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 859us/step - loss: 5006752768.0000 - mae: 50748.3320 - val_loss: 4949777920.0000 - val_mae: 50360.5625\n",
      "Epoch 24/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 1ms/step - loss: 4755348480.0000 - mae: 49575.4297 - val_loss: 4910401536.0000 - val_mae: 50244.9805\n",
      "Epoch 25/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 813us/step - loss: 4771234816.0000 - mae: 49994.9766 - val_loss: 4876162048.0000 - val_mae: 50129.0078\n",
      "Epoch 26/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 760us/step - loss: 4831894016.0000 - mae: 49861.2227 - val_loss: 4851753984.0000 - val_mae: 49844.9609\n",
      "Epoch 27/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 943us/step - loss: 4853082112.0000 - mae: 49396.3516 - val_loss: 4827287552.0000 - val_mae: 49766.7578\n",
      "Epoch 28/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 4519243776.0000 - mae: 48697.3594 - val_loss: 4805418496.0000 - val_mae: 49700.5352\n",
      "Epoch 29/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 744us/step - loss: 4653381632.0000 - mae: 48824.8359 - val_loss: 4785973760.0000 - val_mae: 49626.5117\n",
      "Epoch 30/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 4571381248.0000 - mae: 49004.1797 - val_loss: 4768600576.0000 - val_mae: 49543.9570\n",
      "Epoch 31/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 4544066560.0000 - mae: 48727.1211 - val_loss: 4756042752.0000 - val_mae: 49390.9180\n",
      "Epoch 32/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 4737935872.0000 - mae: 49410.5078 - val_loss: 4739089920.0000 - val_mae: 49408.8594\n",
      "Epoch 33/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 856us/step - loss: 4755367936.0000 - mae: 49444.8828 - val_loss: 4728529920.0000 - val_mae: 49251.9570\n",
      "Epoch 34/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 983us/step - loss: 4477749248.0000 - mae: 48102.6641 - val_loss: 4715792384.0000 - val_mae: 49196.7891\n",
      "Epoch 35/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 4624541696.0000 - mae: 48925.5977 - val_loss: 4707405824.0000 - val_mae: 49081.4336\n",
      "Epoch 36/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 770us/step - loss: 4474116096.0000 - mae: 48336.0430 - val_loss: 4696892928.0000 - val_mae: 49034.5352\n",
      "Epoch 37/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 977us/step - loss: 4502224384.0000 - mae: 48258.8750 - val_loss: 4685581312.0000 - val_mae: 49015.0703\n",
      "Epoch 38/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 960us/step - loss: 4576369664.0000 - mae: 48660.1719 - val_loss: 4680060928.0000 - val_mae: 48872.5391\n",
      "Epoch 39/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 4651052544.0000 - mae: 48933.7969 - val_loss: 4673776640.0000 - val_mae: 48770.4844\n",
      "Epoch 40/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 851us/step - loss: 4587884544.0000 - mae: 48299.1094 - val_loss: 4661730816.0000 - val_mae: 48826.4844\n",
      "Epoch 41/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 990us/step - loss: 4416365568.0000 - mae: 47986.1055 - val_loss: 4652943872.0000 - val_mae: 48839.2422\n",
      "Epoch 42/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 4404473344.0000 - mae: 47958.5469 - val_loss: 4647714816.0000 - val_mae: 48755.8320\n",
      "Epoch 43/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 967us/step - loss: 4524553728.0000 - mae: 48407.9336 - val_loss: 4647618048.0000 - val_mae: 48568.1719\n",
      "Epoch 44/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 989us/step - loss: 4637365760.0000 - mae: 48594.8359 - val_loss: 4632496640.0000 - val_mae: 48704.3633\n",
      "Epoch 45/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 930us/step - loss: 4414740992.0000 - mae: 47993.3633 - val_loss: 4626538496.0000 - val_mae: 48642.5586\n",
      "Epoch 46/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 4705626112.0000 - mae: 49233.5469 - val_loss: 4622363648.0000 - val_mae: 48574.1328\n",
      "Epoch 47/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 950us/step - loss: 4560244224.0000 - mae: 48581.8047 - val_loss: 4613780992.0000 - val_mae: 48614.8438\n",
      "Epoch 48/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 930us/step - loss: 4418208256.0000 - mae: 47975.2578 - val_loss: 4620975104.0000 - val_mae: 48326.5625\n",
      "Epoch 49/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 4536374272.0000 - mae: 48394.7344 - val_loss: 4606001152.0000 - val_mae: 48432.1562\n",
      "Epoch 50/50\n",
      "\u001b[1m409/409\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 1ms/step - loss: 4526328320.0000 - mae: 48652.9336 - val_loss: 4599783424.0000 - val_mae: 48417.0312\n",
      "\u001b[1m128/128\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 524us/step - loss: 4549919232.0000 - mae: 48845.9570\n",
      "Test MAE: 48932.4921875\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n",
    "from sklearn.compose import ColumnTransformer\n",
    "import tensorflow as tf\n",
    "\n",
    "# Load dataset\n",
    "housing_data = pd.read_csv('housing.csv.zip')\n",
    "\n",
    "# Handle missing values by dropping rows with NaN values\n",
    "housing_data_cleaned = housing_data.dropna()\n",
    "\n",
    "# Features and target variable\n",
    "X = housing_data_cleaned[['longitude', 'latitude', 'housing_median_age', 'total_rooms', \n",
    "                          'total_bedrooms', 'population', 'households', 'median_income', 'ocean_proximity']]\n",
    "y = housing_data_cleaned['median_house_value']\n",
    "\n",
    "# Preprocessing\n",
    "numeric_features = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', \n",
    "                    'total_bedrooms', 'population', 'households', 'median_income']\n",
    "categorical_features = ['ocean_proximity']\n",
    "\n",
    "# Create preprocessing pipeline\n",
    "numeric_transformer = StandardScaler()\n",
    "categorical_transformer = OneHotEncoder()\n",
    "\n",
    "preprocessor = ColumnTransformer(\n",
    "    transformers=[\n",
    "        ('num', numeric_transformer, numeric_features),\n",
    "        ('cat', categorical_transformer, categorical_features)\n",
    "    ])\n",
    "\n",
    "# Split the dataset\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Apply preprocessing\n",
    "X_train_processed = preprocessor.fit_transform(X_train)\n",
    "X_test_processed = preprocessor.transform(X_test)\n",
    "\n",
    "# Build the model\n",
    "model = tf.keras.models.Sequential([\n",
    "    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_processed.shape[1],)),\n",
    "    tf.keras.layers.Dense(32, activation='relu'),\n",
    "    tf.keras.layers.Dense(1)  # Output layer for regression\n",
    "])\n",
    "\n",
    "# Compile the model\n",
    "model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])\n",
    "\n",
    "# Train the model\n",
    "model.fit(X_train_processed, y_train, epochs=50, batch_size=32, validation_split=0.2)\n",
    "\n",
    "# Evaluate the model\n",
    "test_loss, test_mae = model.evaluate(X_test_processed, y_test)\n",
    "print(f\"Test MAE: {test_mae}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "55a22b22-37bf-47c6-a101-7f835c9e80e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "\n",
    "# Assuming preprocessor is already fitted on the training data\n",
    "with open('preprocessor.pkl', 'wb') as f:\n",
    "    pickle.dump(preprocessor, f)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "956e0e0d-53a4-4615-b5d5-ee3f6d8c1528",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 59ms/step\n",
      "Predicted House Price: 410611.75\n"
     ]
    }
   ],
   "source": [
    "# Example new house data\n",
    "new_house_data = pd.DataFrame({\n",
    "    'longitude': [-122.23],\n",
    "    'latitude': [37.88],\n",
    "    'housing_median_age': [41],\n",
    "    'total_rooms': [880],\n",
    "    'total_bedrooms': [129],\n",
    "    'population': [322],\n",
    "    'households': [126],\n",
    "    'median_income': [8.3252],\n",
    "    'ocean_proximity': ['NEAR BAY']  # This is a categorical value\n",
    "})\n",
    "\n",
    "# Preprocess the new data (use the same preprocessor pipeline)\n",
    "new_house_processed = preprocessor.transform(new_house_data)\n",
    "\n",
    "# Make the prediction\n",
    "predicted_price = model.predict(new_house_processed)\n",
    "print(f\"Predicted House Price: {predicted_price[0][0]}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "68f499a5-46c7-4d95-9f03-191bd9932145",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING:absl:You are saving your model as an HDF5 file via `model.save()` or `keras.saving.save_model(model)`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')` or `keras.saving.save_model(model, 'my_model.keras')`. \n"
     ]
    }
   ],
   "source": [
    "model.save('house_price_model.h5')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "073902bf-9192-4d5d-ae87-770581a2f9e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 36ms/step\n",
      "Predicted House Price: 410611.75\n"
     ]
    }
   ],
   "source": [
    "# Load the model from the file\n",
    "loaded_model = tf.keras.models.load_model('house_price_model.h5')\n",
    "\n",
    "# Use the loaded model to make predictions (similar to the earlier example)\n",
    "predicted_price = loaded_model.predict(new_house_processed)\n",
    "print(f\"Predicted House Price: {predicted_price[0][0]}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8012ef6c-0f4e-4bca-b21c-8e88a288b27e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "687a6a60-413c-4f5f-b72b-b701bc58915d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
