package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  An identified risk.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Risk  {

  private String uuid;
  private String title;
  private String description;
  private String statement;
  private List<Origin> origins;
  private List<ThreatId> threat-ids;
  private List<Characterization> characterizations;
  private List<MitigatingFactor> mitigating-factors;
  private ZonedDateTime deadline;
  private List<Response> remediations;
  private RiskLog risk-log;
  private List<RelatedObservation> related-observations;
  private String status;
  private List<Property> props;
  private List<Link> links;

}