const express = require('express')
const router = express.Router();
const {db}  = require('../config/firebase')
const similarity = require( 'compute-cosine-similarity' );
const PriorityQueue = require('../class/priorityQueue')

const keywords = ['sumclosed', 'clocktime', 'computation', 'array', 'substringinputeach', 'permutationinputthe', 'xoutputfor', 'pmodq', 'arraythe', 'java', 'walktime', 'zeroinputthe', 'forest', 'treesthere', 'locks', 'palindromewe', 'shufflingtime', 'outputcopyyesnonotetest', 'polycarps', 'stones', 'palindromic', 'creepinessinputthe', 'operationsin', 'constraintstime', 'colors', 'trainstime', 'smallestpermutation', 'cell', 'robottime', 'linguisticstime', 'stringfind', 'operationsinputthe', 'permutationtime', 'integer', 'integershere', 'gambling', 'pointer', 'treesmisha', 'distances', 'swapping', 'arrangementinputthe', 'decreasing', 'queries', 'ijx', 'distance', 'bitwise', 'vertex', 'permutationinputthere', 'clockoutputfor', 'participants', 'weightinputthe', 'pipes', 'permutation', 'reduce', 'trains', 'vertices', 'map', 'abc', 'trapsexampleinputcopy', 'path', 'clock', 'minimizes', 'difftime', 'lexicographically', 'remainder', 'bipartite', 'noexampleinputcopycabcabababbabcbbaacbbcaabababccbbababaacbaaboutputcopyyesnoyesyesno', 'weights', 'maximized', 'multiset', 'store', 'universe', 'sequences', 'multisetit', 'shuffled', 'substringstime', 'digits', 'trees', 'sum', 'subrectangle', 'carriages', 'sumclosedin', 'swappingtime', 'testcase', 'grid', 'arrayinputthe', 'traps', 'tree', 'xor', 'trapsinputthe', 'shift', 'gensokyorecall', 'taskinputthe', 'puzzles', 'sequence', 'cellsexampleinputcopy', 'infectedthe', 'patchouli', 'segment', 'brackets', 'moves', 'problemtime', 'paths', 'adaptiveinputthe', 'arrangements', 'operations', 'stripe', 'nodesthe', 'treeoutputprint', 'bracketsthe', 'rounds', 'sequenceit', 'coins', 'orz', 'casexmodymodymodzmodzmodxmod', 'palindrome', 'bracket', 'groupstime', 'solutions', 'graphs', 'treethe', 'producttime', 'railways', 'concatenating', 'operationsexampleinputcopy', 'purchaseexampleinputcopy', 'cells', 'pedestals', 'shortest', 'speeds', 'secondsmemory', 'bishop', 'packing', 'token', 'inputoutputstandard', 'consecutive', 'enchanted', 'circular', 'segmentstime', 'constraintsinputthe', 'distinct',
'orztime', 'treestime', 'platform', 'evenexampleinputcopy', 'rows', 'mushroomsit', 'optimallyinputthe', 'reverse', 'mushroom', 'substrings', 'board', 'casino', 'goods', 'operationsinputeach', 'aij', 'subtree', 'minimizationtime', 'nodes', 'permutationoutputoutput', 'compute', 'minimaxtime', 'minimal', 'coloringtime', 'determine', 'arrayoutputfor', 'tokens', 'pairsthe', 'subarrays', 'testcasesthe', 'trap', 'bishopinputthe', 'integersthe', 'arrangement', 'sandtime', 'euclid', 'rearrangement', 'rounding', 'dominoestime', 'answerexampleinputcopy', 'bishoptime', 'creeptime', 'carriage', 'city', 'row', 'energy', 'subarray', 'matrixtime', 'knipipiinputthere', 'segmentsexampleinputcopy', 'subarraystime', 'lockstime', 'test', 'binary', 'vvlcmb', 'mushrooms', 'concatenation', 'graph', 'marathontime', 'exceed', 'subsequence', 'pilesit', 'treetime', 'permutationthe', 'permutations', 'indices', 'marathon', 'optimal', 'domino', 'constraints', 'pedestal', 'integers', 'algorithm', 'constraint', 'decrement', 'permutationforces', 'digit', 'color', 'tokensthe', 'treeit', 'megabytesinputstandard', 'gamblingtime', 'sumclosedinputthe', 'queue', 'pilesoutputfor', 'maximizationtime', 'segments', 'mathematics', 'eveninputeach', 'purchases', 'walking', 'pathtime', 'tasks', 'operation', 'shuffledyou', 'treeyou', 'integerlets', 'chessboard', 'abbcacn', 'sitting', 'systems', 'cities', 'universetime', 'swap', 'palindromein', 'swaps', 'palindromes', 'matrix', 'platforms', 'maximum', 'robot', 'taskstime', 'railway', 'reversaltime', 'zeroes', 'shuffling', 'substring', 'ai', 'sumtime', 'treeeach', 'blocks', 'smallest', 'conditions', 'good', 'lock', 'jm', 'infected', 'balanced', 'concatenate', 'strings', 'pairs', 'minimize', 'segmentits', 'pipe', 'keshi', 'trapstime', 'walk', 'ij', 'roads', 'treethen', 'alphabet', 'shuffle', 'dividing', 'task', 'guessingtime', 'numberstest', 'sort', 'permuting', 'arraytime', 'stringtime', 'groups', 'arrayit', 'shoes', 'string', 'piles', 'pile', 'columns', 'mushroomstest', 'arrays', 'dominoes', 'sand']

const idfVector = [0.0, 4.605170185988092, 1.7147984280919266, 0.123123123131231, 0.0, 0.0, 0.0, 4.605170185988092, 0.0, 3.2188758248682006, 0.0, 0.0, 0.0, 4.605170185988092, 0.6733445532637655, 0.0, 0.0, 0.0, 3.506557897319982, 4.605170185988092, 1.9661128563728327, 4.605170185988092, 1.7719568419318754, 0.0, 4.605170185988092, 0.0, 0.0, 0.0, 0.0, 0.0, 2.5257286443082556, 0.0, 0.0, 2.302585092994046, 0.0, 0.0, 0.0, 3.912023005428146, 0.0, 4.605170185988092, 3.506557897319982, 3.912023005428146, 3.912023005428146, 4.605170185988092, 0.0, 4.605170185988092, 0.0, 0.0, 4.605170185988092, 0.0, 4.605170185988092, 3.912023005428146, 0.0, 4.605170185988092, 4.605170185988092, 3.912023005428146, 0.0, 0.9942522733438669, 4.605170185988092, 4.605170185988092, 4.605170185988092, 0.0, 0.0, 3.2188758248682006, 2.407945608651872, 4.605170185988092, 0.0, 4.605170185988092, 0.5276327420823719, 0.0, 4.605170185988092, 0.0, 3.912023005428146, 0.0, 4.605170185988092, 4.605170185988092, 4.605170185988092, 4.605170185988092, 4.605170185988092, 4.605170185988092, 4.605170185988092, 0.0, 1.5606477482646683, 2.407945608651872, 0.0, 2.5257286443082556, 0.0, 0.0, 2.659260036932778, 2.995732273553991, 4.605170185988092, 3.912023005428146, 0.0, 3.912023005428146, 0.0, 0.0, 4.605170185988092, 2.407945608651872, 3.2188758248682006, 4.605170185988092, 4.605170185988092, 0.0, 0.0, 0.0, 0.0, 3.912023005428146, 0.0, 3.912023005428146, 0.0, 0.0, 2.407945608651872, 0.0, 1.7719568419318754, 3.912023005428146, 0.0, 3.506557897319982, 2.302585092994046, 4.605170185988092, 2.207274913189721, 4.605170185988092, 4.605170185988092, 4.605170185988092, 4.605170185988092, 3.912023005428146, 0.0, 3.506557897319982, 2.302585092994046, 4.605170185988092, 4.605170185988092, 4.605170185988092, 3.506557897319982, 2.0402208285265546, 0.0, 2.5257286443082556, 0.0, 4.605170185988092, 4.605170185988092, 3.912023005428146, 3.912023005428146, 3.912023005428146, 4.605170185988092, 0.0, 0.0, 0.0, 0.0, 0.0, 4.605170185988092, 0.0, 3.506557897319982, 4.605170185988092, 0.47803580094299974,
             2.0402208285265546, 4.605170185988092, 3.912023005428146, 4.605170185988092, 0.0, 0.0, 4.605170185988092, 0.0, 1.3093333199837622, 3.912023005428146, 4.605170185988092, 4.605170185988092, 4.605170185988092, 3.912023005428146, 0.0, 0.0, 4.605170185988092, 0.083381608939051, 0.0, 0.0, 4.605170185988092, 4.605170185988092, 0.0, 0.0, 0.0, 4.605170185988092, 2.659260036932778, 0.0, 4.605170185988092, 3.912023005428146, 3.912023005428146, 0.0, 3.912023005428146, 4.605170185988092, 4.605170185988092, 4.605170185988092, 0.0, 0.0, 3.2188758248682006, 2.659260036932778, 0.0, 3.2188758248682006, 0.0, 4.605170185988092, 0.0, 0.0, 0.0, 0.0, 3.912023005428146, 0.0, 0.0, 0.0, 4.605170185988092, 4.605170185988092, 2.659260036932778, 2.995732273553991, 0.07257069283483537, 0.0, 3.2188758248682006, 3.912023005428146, 0.0, 2.659260036932778, 1.2039728043259361, 4.605170185988092, 4.605170185988092, 2.995732273553991, 4.605170185988092, 0.0, 0.0, 0.0, 3.912023005428146, 0.0, 4.605170185988092, 2.302585092994046, 0.0, 3.912023005428146, 0.0, 0.0, 4.605170185988092, 3.506557897319982, 0.0, 0.0, 0.0, 4.605170185988092, 0.0, 3.506557897319982, 0.0, 4.605170185988092, 4.605170185988092, 0.0, 0.0, 3.912023005428146, 2.120263536200091, 0.0, 2.5257286443082556, 2.5257286443082556, 2.302585092994046, 0.0, 0.0, 2.8134107167600364, 2.8134107167600364, 1.171182981502945, 4.605170185988092, 2.5257286443082556, 4.605170185988092, 0.0, 4.605170185988092, 2.995732273553991, 2.302585092994046, 0.0, 0.0, 0.0, 0.0, 0.0, 4.605170185988092, 2.8134107167600364, 0.0, 4.605170185988092, 3.912023005428146, 0.0, 4.605170185988092, 0.0, 4.605170185988092, 0.0, 0.0, 0.0, 4.605170185988092, 3.912023005428146, 0.0, 0.0, 0.0, 4.605170185988092, 3.506557897319982, 3.506557897319982, 4.605170185988092, 4.605170185988092, 4.605170185988092, 0.0, 0.0, 0.0, 4.605170185988092, 3.506557897319982, 2.207274913189721, 3.2188758248682006, 2.995732273553991, 4.605170185988092, 3.2188758248682006, 2.995732273553991, 4.605170185988092, 4.605170185988092]


const Search = async(req,res)=>{
     
    let   queryString = req.body.queryString
    queryString = queryString.replace(/[^a-zA-Z ]/g, ""); 
    let words = queryString.split(' ');
    const map = new Map();

    for(let i=0;i<keywords.length;i++)   
         map.set(keywords[i] , i);      

    let total = 0 
    let v1 = new Array(301).fill(0);

   for(let i=0;i<words.length;i++){
        if(map.get(words[i])!=undefined){
            let index = map.get(words[i]);
            v1[index]= v1[index] + 1;
            total = total + 1
        }
   }

   if(total == 0 ) return res.status(200).json({msg : "sorry we don't have enough data"}) 


   const queue = new PriorityQueue();
   const index = new Map();  
 
   for(let i=0;i<301;i++)v1[i] = (v1[i]/total) * idfVector[i];
 
   const data = await db.collection('questions').get();
   data.forEach((doc)=>{
      const vector = doc.data().vector;
      const docId = String(doc.data().count)

      const s = similarity( v1 , vector ); 
        if(s > 0 ){
            console.log(s);
            queue.push(s);
            if(index.get(s) == undefined){
            index.set(s ,[String(docId)]); 
            }else{
            const arr = index.get(s);
            arr.push(String(docId)); 
            index.set(s , arr);
            } 
        }
   })
    
   let ans = [];
    
   while(!queue.isEmpty() && ans.length < 10){
      const val = queue.pop(); 
      ans.push(...index.get(val));
   }
  
   let response = [];
   for(let i=0;i<ans.length;i++){
       const data =await db.collection('questions').doc(ans[i]).get();
       response.push(data.data())
   }  

    return res.status(200).json({
        response : response
    })
}



router
     .route('/search')
     .post(Search) 
    
    
module.exports = {
        Router: router,
};
      