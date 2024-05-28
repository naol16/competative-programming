<h2><a href="https://leetcode.com/problems/heaters/">475. Heaters</a></h2><h3>Medium</h3><hr><div><p>Wi<span data-id="3a04e6ea-f894-47be-ad85-3cd1c7d06b65" class="monica-mark monica-mark-3a04e6ea-f894-47be-ad85-3cd1c7d06b65" style="background-color: #FAFF0A72; cursor: pointer; ">nter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.</span></p>

<p><span data-id="3a04e6ea-f894-47be-ad85-3cd1c7d06b65" class="monica-mark monica-mark-3a04e6ea-f894-47be-ad85-3cd1c7d06b65" style="background-color: #FAFF0A72; cursor: pointer; ">Every house can be warmed, as long as the house is w</span>ithin the heater's warm radius range.&nbsp;</p>

<p>Given the positions of <code>houses</code> and <code>heaters</code> on a horizontal line, return <em>the minimum radius standard of heaters&nbsp;so that those heaters could cover all houses.</em></p>

<p><strong>Notice</strong> <span data-id="4f9b4a09-9480-4988-8fdf-5ad5ab4e326c" class="monica-mark monica-mark-4f9b4a09-9480-4988-8fdf-5ad5ab4e326c" style="background-color: #FAFF0A72; cursor: pointer; ">that&nbsp;all the </span><code><span data-id="4f9b4a09-9480-4988-8fdf-5ad5ab4e326c" class="monica-mark monica-mark-4f9b4a09-9480-4988-8fdf-5ad5ab4e326c" style="background-color: #FAFF0A72; cursor: pointer; ">heaters</span></code> follow your radius standard, and the warm radius will the same.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> houses = [1,2,3], heaters = [2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 2:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> houses = [1,2,3,4], heaters = [1,4]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The two heaters were placed at positions 1 and 4. We need to use a radius 1 standard, then all the houses can be warmed.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 3:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> houses = [1,5], heaters = [2]
<strong>Output:</strong> 3
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= houses.length, heaters.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= houses[i], heaters[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>